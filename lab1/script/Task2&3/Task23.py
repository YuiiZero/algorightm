from FileService import writeTo

class Fibonacci:
  def fibonacci(self, n: int) -> int:
    if (not isinstance(n, int)):
      raise TypeError('Argument must be integer')

    if (n < 0):
      raise ValueError('Argument must be positive')

    if (n == 0 or n == 1):
      return n

    a, b = 0, 1

    for _ in range(2, n + 1):
      b, a = b + a, b
  
  def writeFibonacci(self, inputPath: str, outputPath: str):
    writeTo(self.fibonacci, inputPath, outputPath)

  def findLastDigit(self, n: int) -> int:
    return self.fibonacci(n) % 10

  def writeFindLastDigit(self, inputPath: str, outputPath: str):
    writeTo(self.findLastDigit, inputPath, outputPath)
    
fibonacci = Fibonacci()
