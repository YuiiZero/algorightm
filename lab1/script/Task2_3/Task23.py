from FileService import write_to

class Fibonacci:
  def fibonacci(self, string: str) -> int:
    self._assertInt(string)

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

  def find_last_digit(self, string: str) -> int:
    self._assertInt(string)

    return self.fibonacci(string) % 10

  def write_find_last_digit(self, input_path: str, output_path: str):
    write_to(self.find_last_digit, input_path, output_path)

  def _assertInt(self, string: str) -> None:
    if (not isinstance(string, str)):
      raise TypeError('Argument is not integer.')

    string = string.strip().replace('-', '').replace('+', '')

    if len(string) > 1:
      string = string.lstrip('0')

    if not string.isdigit():
      raise TypeError('Argument is not integer.')
    
fibonacci = Fibonacci()
