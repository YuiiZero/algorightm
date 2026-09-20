from FileService import write_to

class Fibonacci:
  def fibonacci(self, string: str) -> int:
    n = int(string)

    if (n < 0):
      raise ValueError('Argument must be positive')

    if (n == 0 or n == 1):
      return n

    a, b = 0, 1

    for _ in range(2, n + 1):
      b, a = b + a, b

    return b
  
  def write_fibonacci(self, input_path: str, output_path: str):
    write_to(self.fibonacci, input_path, output_path)

  def find_last_digit(self, n: int) -> int:
    return self.fibonacci(n) % 10

  def write_find_last_digit(self, input_path: str, output_path: str):
    write_to(self.find_last_digit, input_path, output_path)
    
fibonacci = Fibonacci()
