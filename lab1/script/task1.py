class SumClass:
  def add(self, string: str) -> int:
    return sum(self._parseInts(string))

  def addSquared(self, string: str) -> int:
    numbers = self._parseInts(string)

    return numbers[0] + numbers[1]**2  

  def addFromFile(self, inputPath: str, outputPath: str) -> None:
    with open(inputPath) as inputFile:
      string = inputFile.readline()
      
    with open(outputPath, 'w') as outputFile:
      outputFile.write(str(self.add(string)))

  def addSquaredFromFile(self, inputPath: str, outputPath: str) -> None:
    with open(inputPath) as inputFile:
      string = inputFile.readline()
      
    with open(outputPath, 'w') as outputFile:
      outputFile.write(str(self.addSquared(string)))

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

calculator = SumClass()

print(calculator.addSquaredFromFile("./input.txt", "./output.txt"))