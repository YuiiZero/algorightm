from FileService import writeTo

class Add:
  def add(self, string: str) -> int:
    return sum(self._parseInts(string))

  def writeAdd(self, inputPath: str, outputPath: str) -> None:
    writeTo(self.add, inputPath, outputPath)

  def addSquared(self, string: str) -> int:
    numbers = self._parseInts(string)

    return numbers[0] + numbers[1]**2  

  def writeAddSquared(self, inputPath: str, outputPath: str) -> None:
    writeTo(self.addSquared, inputPath, outputPath)

  def _parseInts(self, string: str) -> list[int]:
    numbers = list(map(lambda x: int(x), string.split(' ')))

    self._assertChecks(numbers)
    
    return numbers

  def _assertChecks(self, numbers: list[int]) -> None:
    if (len(numbers) != 2 or any(list(map(lambda num: not isinstance(num, int), numbers)))):
      raise TypeError('Wrong string format. Input string must contain exactly two integer numbers.')
    
    if (any(list(map(lambda x: not self._isValidRange(x), numbers)))):
      raise TypeError('Numbers should be in range -10^9 and 10^9.')

  def _isValidRange(self, num: int) -> bool:
    return num <= 10**9 and num >= -10**9

calculator = Add()
