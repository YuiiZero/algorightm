from typing import Callable

def writeTo(func: Callable[[str], int], inputPath: str, outputPath: str) -> None:
    with open(inputPath) as inputFile:
      string = inputFile.readline()
      
    with open(outputPath, 'w') as outputFile:
      outputFile.write(str(func(string)))
