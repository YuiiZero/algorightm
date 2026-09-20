from datetime import datetime

LOG_FILE = "test_execution.log"

def write_log(
    test_name: str,
    args,
    expected,
    passed,
    test_result: dict
):
  with open(LOG_FILE, "a", encoding="utf-8") as file:
    file.write("=" * 60 + "\n")
    file.write(f"TIME: {datetime.now()}\n")
    file.write(f"TEST: {test_name}\n")
    file.write(f"STATUS: {'PASSED' if passed else 'FAILED'}\n")
    file.write(f"INPUT: {args}\n")
    file.write(f"EXPECTED: {expected}\n")
    file.write(f"ACTUAL: {test_result['result']}\n")

    if test_result["time"] is not None:
      file.write(
        f"EXECUTION TIME: {test_result['time']:.6f} s\n"
      )
      file.write(
        f"TIME LIMIT: {test_result['time_passed']}\n"
      )
    else:
      file.write("EXECUTION TIME: not measured\n")

    if test_result["memory"] is not None:
      file.write(
        f"MEMORY: {test_result['memory'] / 1024:.2f} KB\n"
      )
      file.write(
        f"MEMORY LIMIT: {test_result['memory_passed']}\n"
      )
    else:
      file.write("MEMORY: not measured\n")

    file.write("=" * 60 + "\n\n")