from typing import Callable

def write_to(func: Callable[[str], int], input_path: str, output_path: str) -> None:
    with open(input_path) as inputFile:
      string = inputFile.readline()
      
    with open(output_path, 'w') as outputFile:
      outputFile.write(str(func(string)))

def read_output(output_path: str) -> int:
   with open(output_path) as f:
      return int(f.readline())

def write_input(input_path: str, ints: list[int]) -> None:
   with open(input_path, 'w') as f:
      f.write(' '.join(map(lambda x: str(x), ints)))

def read_input(input_path: str) -> list[int]:
   with open(input_path) as f:
      return list(map(lambda x: int(x), f.readline().strip().split(' ')))