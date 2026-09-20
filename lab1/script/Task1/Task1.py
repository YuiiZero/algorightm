from FileService import write_to

class Add:
  def add(self, string: str) -> int:
    return sum(self._parse_ints(string))

  def write_add(self, input_path: str, output_path: str) -> None:
    write_to(self.add, input_path, output_path)

  def add_squared(self, string: str) -> int:
    numbers = self._parse_ints(string)

    return numbers[0] + numbers[1]**2  

  def write_add_squared(self, input_path: str, output_path: str) -> None:
    write_to(self.add_squared, input_path, output_path)

  def _parse_ints(self, string: str) -> list[int]:
    numbers = list(map(lambda x: int(x), string.split(' ')))

    self._assert_checks(numbers)
    
    return numbers

  def _assert_checks(self, numbers: list[int]) -> None:
    if (len(numbers) != 2 or any(list(map(lambda num: not isinstance(num, int), numbers)))):
      raise TypeError('Wrong string format. Input string must contain exactly two integer numbers.')
    
    if (any(list(map(lambda x: not self._is_valid_range(x), numbers)))):
      raise TypeError('Numbers should be in range -10^9 and 10^9.')

  def _is_valid_range(self, num: int) -> bool:
    return num <= 10**9 and num >= -10**9

calculator = Add()
