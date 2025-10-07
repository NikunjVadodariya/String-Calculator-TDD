import re


class NegativeNumberError(Exception):
    pass


def add(nums_str: str) -> int:
    if not nums_str or nums_str.strip() == "":
        return 0

    delimiter = ",|\n"
    if nums_str.startswith("//"):
        match = re.match(r"//(.+)\n(.*)", nums_str, re.DOTALL)
        if match:
            delimiter = re.escape(match.group(1))
            nums_str = match.group(2)

    numbers_str = re.split(delimiter, nums_str)
    numbers = []
    for num in numbers_str:
        try:
            numbers.append(int(num))
        except:
            pass
    negatives = [n for n in numbers if n < 0]
    if negatives:
        raise NegativeNumberError(
            f"negative numbers not allowed {','.join(map(str, negatives))}"
        )

    return sum(numbers)
