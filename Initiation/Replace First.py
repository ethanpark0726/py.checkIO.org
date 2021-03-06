# https://py.checkio.org/en/mission/replace-first/

from typing import Iterable

def replace_first(items: list) -> Iterable:
    # your code here
    if len(items) <= 1:
        return items
    else:
        b = items[1:len(items)]
        b.append(items[0])

        return b

if __name__ == "__main__":
    print("Example:")
    print(list(replace_first([1, 2, 3, 4])))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(replace_first([1, 2, 3, 4])) == [2, 3, 4, 1]
    assert list(replace_first([1])) == [1]
    assert list(replace_first([])) == []
    print("Coding complete? Click 'Check' to earn cool rewards!")
