import time
import random
import tracemalloc

from typing import Callable

from FileService import *

from Task1 import calculator
from Task2_3 import fibonacci


def expected_fibonacci(n: int) -> int:
  a, b = 0, 1

  for _ in range(n):
    a, b = b, a + b

  return a


def int_check(
    func: Callable[..., int], time_limit: float | None, memory_limit: int | None, *args
):
  speed_check = time_limit is not None
  memory_check = memory_limit is not None

  if memory_check:
    tracemalloc.start()

  if speed_check:
    start = time.perf_counter()

  try:
    result = func(*args)

    if speed_check:
      elapsed = time.perf_counter() - start
    else:
      elapsed = None

    if memory_check:
      _, peak_memory = tracemalloc.get_traced_memory()
    else:
      peak_memory = None

  finally:
    if memory_check:
      tracemalloc.stop()

  return {
    "result": result,
    "time": elapsed,
    "memory": peak_memory,
    "time_passed": (elapsed <= time_limit if speed_check else None),
    "memory_passed": (peak_memory <= memory_limit if memory_check else None),
  }


def write_check(
    func: Callable[[str, str], None],
    time_limit: float | None,
    memory_limit: int | None,
    input_path: str,
    output_path: str,
):
  speed_check = time_limit is not None
  memory_check = memory_limit is not None

  if memory_check:
    tracemalloc.start()

  if speed_check:
    start = time.perf_counter()

  try:
    func(input_path, output_path)

    if speed_check:
      elapsed = time.perf_counter() - start
    else:
      elapsed = None

    if memory_check:
      _, peak_memory = tracemalloc.get_traced_memory()
    else:
      peak_memory = None

  finally:
    if memory_check:
      tracemalloc.stop()

  return {
    "result": read_output(output_path),
    "time": elapsed,
    "memory": peak_memory,
    "time_passed": (elapsed <= time_limit if speed_check else None),
    "memory_passed": (peak_memory <= memory_limit if memory_check else None),
  }


def test_add():
  for _ in range(50):
    first = random.randint(-(10**9), 10**9)
    second = random.randint(-(10**9), 10**9)

    check_result = int_check(calculator.add, None, None, f"{first} {second}")

    assert check_result["result"] == first + second


def test_write_add():
  for _ in range(50):
    first = random.randint(-(10**9), 10**9)
    second = random.randint(-(10**9), 10**9)

    write_input("input.txt", [first, second])

    check_result = write_check(
        calculator.write_add, None, None, "input.txt", "output.txt"
    )

    assert check_result["result"] == first + second


def test_add_squared():
  for _ in range(50):
    first = random.randint(-(10**9), 10**9)
    second = random.randint(-(10**9), 10**9)

    check_result = int_check(calculator.add_squared, None, None, f"{first} {second}")

    assert check_result["result"] == first + second**2


def test_write_add_squared():
  for _ in range(50):
    first = random.randint(-(10**9), 10**9)
    second = random.randint(-(10**9), 10**9)

    write_input("input.txt", [first, second])

    check_result = write_check(
        calculator.write_add_squared, None, None, "input.txt", "output.txt"
    )

    assert check_result["result"] == first + second**2


def test_write_fibonacci():
  for _ in range(20):
    n = random.randint(0, 45)

    write_input("input.txt", [n])

    check_result = write_check(
        fibonacci.write_fibonacci, None, None, "input.txt", "output.txt"
    )

    assert check_result["result"] == expected_fibonacci(n)


def test_write_fibonacci_last_digit():
  for _ in range(5):
    n = random.randint(0, 45)

    write_input("input.txt", [n])

    check_result = write_check(
        fibonacci.write_find_last_digit, 5, 512 * 10**6, "input.txt", "output.txt"
    )

    assert check_result["result"] == expected_fibonacci(n) % 10

    assert check_result["time_passed"], (
        f"Time limit exceeded: " f"{check_result['time']:.6f}s > 5s"
    )

    assert check_result["memory_passed"], (
        f"Memory limit exceeded: "
        f"{check_result['memory'] / 1024**2:.2f} MB > 512 MB"
    )
