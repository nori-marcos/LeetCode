from typing import List

test = [1, 2, 3]


def plus_one(digits: List[int]) -> List[int]:
    integer_str = "".join(map(str, digits))
    integer = int(integer_str) + 1
    integer_str = str(integer)

    return list(integer_str)


print(plus_one(test))
