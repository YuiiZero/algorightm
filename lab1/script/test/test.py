import pytest
import time
import random
import tracemalloc

from typing import Callable

from FileService import *

from Task1 import calculator
from Task2_3 import fibonacci
from .TestLogger import write_log

# =========================
# Helper functions
# =========================

def expected_fibonacci(n: int) -> int:
  a, b = 0, 1

  for _ in range(n):
    a, b = b, a + b

  return a


def int_check(
    func: Callable[..., int],
    expected: int,
    time_limit: float | None,
    memory_limit: int | None,
    *args
):
  if memory_limit is not None:
    tracemalloc.start()

  if time_limit is not None:
    start = time.perf_counter()

  try:
    result = func(*args)

    elapsed = (
      time.perf_counter() - start
      if time_limit is not None
      else None
    )

    if memory_limit is not None:
      _, peak_memory = tracemalloc.get_traced_memory()
    else:
      peak_memory = None

  finally:
    if memory_limit is not None:
      tracemalloc.stop()

  result_passed = result == expected

  time_passed = (
    elapsed <= time_limit
    if time_limit is not None
    else None
  )

  memory_passed = (
    peak_memory <= memory_limit
    if memory_limit is not None
    else None
  )

  test_passed = (
    result_passed
    and (time_passed is not False)
    and (memory_passed is not False)
  )

  test_result = {
    "result": result,
    "time": elapsed,
    "memory": peak_memory,
    "time_passed": time_passed,
    "memory_passed": memory_passed,
  }

  write_log(
    test_name=func.__name__,
    args=args,
    expected=expected,
    passed=test_passed,
    test_result=test_result,
  )

  return test_result


def write_check(
    func: Callable[[str, str], None],
    expected: int,
    time_limit: float | None,
    memory_limit: int | None,
    input_path: str,
    output_path: str,
):
  if memory_limit is not None:
      tracemalloc.start()

  if time_limit is not None:
    start = time.perf_counter()

  try:
    func(input_path, output_path)
    result = read_output(output_path)

    elapsed = (
      time.perf_counter() - start
      if time_limit is not None
      else None
    )

    if memory_limit is not None:
      _, peak_memory = tracemalloc.get_traced_memory()
    else:
      peak_memory = None

  finally:
    if memory_limit is not None:
      tracemalloc.stop()

  result_passed = int(result) == expected

  time_passed = (
    elapsed <= time_limit
    if time_limit is not None
    else None
  )

  memory_passed = (
    peak_memory <= memory_limit
    if memory_limit is not None
    else None
  )

  test_passed = (
    result_passed
    and (time_passed is not False)
    and (memory_passed is not False)
  )

  test_result = {
    "result": result,
    "time": elapsed,
    "memory": peak_memory,
    "time_passed": time_passed,
    "memory_passed": memory_passed,
  }

  write_log(
    test_name=func.__name__,
    args=read_input(input_path),
    expected=expected,
    passed=test_passed,
    test_result=test_result,
  )

  return test_result

# =========================
# Add funcs: random values
# =========================

def test_add():
  for _ in range(50):
    first = random.randint(-(10**9), 10**9)
    second = random.randint(-(10**9), 10**9)

    expected = first + second

    check_result = int_check(
      calculator.add,
      expected,
      None,
      None,
      f"{first} {second}"
    )

    assert check_result["result"] == expected


def test_write_add():
  for _ in range(50):
    first = random.randint(-(10**9), 10**9)
    second = random.randint(-(10**9), 10**9)

    expected = first + second

    write_input("input.txt", [first, second])

    check_result = write_check(
      calculator.write_add,
      expected,
      None,
      None,
      "input.txt",
      "output.txt"
    )

    assert check_result["result"] == expected


def test_add_squared():
  for _ in range(50):
    first = random.randint(-(10**9), 10**9)
    second = random.randint(-(10**9), 10**9)

    expected = first + second**2

    check_result = int_check(
      calculator.add_squared,
      expected,
      None,
      None,
      f"{first} {second}"
    )

    assert check_result["result"] == expected


def test_write_add_squared():
  for _ in range(50):
    first = random.randint(-(10**9), 10**9)
    second = random.randint(-(10**9), 10**9)

    expected = first + second**2

    write_input("input.txt", [first, second])

    check_result = write_check(
      calculator.write_add_squared,
      expected,
      None,
      None,
      "input.txt",
      "output.txt"
    )

    assert check_result["result"] == expected


# =========================
# Fibonacci: random values
# =========================

def test_write_fibonacci():
  for _ in range(20):
    n = random.randint(0, 45)

    expected = expected_fibonacci(n)

    write_input("input.txt", [n])

    check_result = write_check(
      fibonacci.write_fibonacci,
      expected,
      None,
      None,
      "input.txt",
      "output.txt"
    )

    assert check_result["result"] == expected


def test_write_fibonacci_last_digit():
  for _ in range(5):
    n = random.randint(0, 45)

    expected = expected_fibonacci(n) % 10

    write_input("input.txt", [n])

    check_result = write_check(
      fibonacci.write_find_last_digit,
      expected,
      5,
      512 * 10**6,
      "input.txt",
      "output.txt"
    )

    assert check_result["result"] == expected

    assert check_result["time_passed"], (
      f"Time limit exceeded: "
      f"{check_result['time']:.6f}s > 5s"
    )

    assert check_result["memory_passed"], (
      f"Memory limit exceeded: "
      f"{check_result['memory'] / 1024**2:.2f} MB > 512 MB"
    )


# =========================
# Add funcs: edge cases
# =========================

def test_add_min_values():
  expected = -2 * 10**9

  check_result = int_check(
    calculator.add,
    expected,
    None,
    None,
    f"{-10**9} {-10**9}"
  )

  assert check_result["result"] == expected


def test_add_max_values():
  expected = 2 * 10**9

  check_result = int_check(
    calculator.add,
    expected,
    None,
    None,
    f"{10**9} {10**9}"
  )

  assert check_result["result"] == expected


def test_add_min_max_values():
  expected = 0

  check_result = int_check(
    calculator.add,
    expected,
    None,
    None,
    f"{-10**9} {10**9}"
  )

  assert check_result["result"] == expected


def test_add_zero_values():
  expected = 0

  check_result = int_check(
    calculator.add,
    expected,
    None,
    None,
    "0 0"
  )

  assert check_result["result"] == expected


def test_add_squared_min_values():
  expected = -10**9 + (-10**9)**2

  check_result = int_check(
    calculator.add_squared,
    expected,
    None,
    None,
    f"{-10**9} {-10**9}"
  )

  assert check_result["result"] == expected


def test_add_squared_max_values():
  expected = 10**9 + (10**9)**2

  check_result = int_check(
    calculator.add_squared,
    expected,
    None,
    None,
    f"{10**9} {10**9}"
  )

  assert check_result["result"] == expected


def test_add_squared_zero_values():
  expected = 0

  check_result = int_check(
    calculator.add_squared,
    expected,
    None,
    None,
    "0 0"
  )

  assert check_result["result"] == expected


# =========================
# Fibonacci: edge cases
# =========================

def test_fibonacci_zero():
  expected = 0

  check_result = int_check(
    fibonacci.fibonacci,
    expected,
    None,
    None,
    "0"
  )

  assert check_result["result"] == expected


def test_fibonacci_one():
  expected = 1

  check_result = int_check(
    fibonacci.fibonacci,
    expected,
    None,
    None,
    "1"
  )

  assert check_result["result"] == expected


def test_fibonacci_two():
  expected = 1

  check_result = int_check(
    fibonacci.fibonacci,
    expected,
    None,
    None,
    "2"
  )

  assert check_result["result"] == expected


def test_fibonacci_45():
  expected = 1134903170

  check_result = int_check(
    fibonacci.fibonacci,
    expected,
    None,
    None,
    "45"
  )

  assert check_result["result"] == expected


def test_fibonacci_last_digit_zero():
  expected = 0

  check_result = int_check(
    fibonacci.find_last_digit,
    expected,
    None,
    None,
    "0"
  )

  assert check_result["result"] == expected


def test_fibonacci_last_digit_one():
  expected = 1

  check_result = int_check(
    fibonacci.find_last_digit,
    expected,
    None,
    None,
    "1"
  )

  assert check_result["result"] == expected


def test_fibonacci_last_digit_45():
  expected = 0

  check_result = int_check(
    fibonacci.find_last_digit,
    expected,
    None,
    None,
    "45"
  )

  assert check_result["result"] == expected


# =========================
# Fibonacci: write edge cases
# =========================

def test_write_fibonacci_zero():
  expected = 0

  write_input("input.txt", [0])

  check_result = write_check(
    fibonacci.write_fibonacci,
    expected,
    None,
    None,
    "input.txt",
    "output.txt"
  )

  assert check_result["result"] == expected


def test_write_fibonacci_one():
  expected = 1

  write_input("input.txt", [1])

  check_result = write_check(
    fibonacci.write_fibonacci,
    expected,
    None,
    None,
    "input.txt",
    "output.txt"
  )

  assert check_result["result"] == expected


def test_write_fibonacci_45():
  expected = 1134903170

  write_input("input.txt", [45])

  check_result = write_check(
    fibonacci.write_fibonacci,
    expected,
    None,
    None,
    "input.txt",
    "output.txt"
  )

  assert check_result["result"] == expected


def test_write_fibonacci_last_digit_zero():
  expected = 0

  write_input("input.txt", [0])

  check_result = write_check(
    fibonacci.write_find_last_digit,
    expected,
    None,
    None,
    "input.txt",
    "output.txt"
  )

  assert check_result["result"] == expected


def test_write_fibonacci_last_digit_45():
  expected = 0

  write_input("input.txt", [45])

  check_result = write_check(
    fibonacci.write_find_last_digit,
    expected,
    None,
    None,
    "input.txt",
    "output.txt"
  )

  assert check_result["result"] == expected