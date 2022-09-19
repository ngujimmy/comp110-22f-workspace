"""EX04 List."""
__author__ = "730574005"


def all(int_list: list[int], test: int) -> bool:
    """Function that verifies if list contains all the same integer."""
    if len(int_list) == 0:
        return False
    i: int = 0
    match: int = test
    while i < len(int_list):
        if match == int_list[i]:
            match = int_list[i]
            i += 1 
        else:
            print(False)
            return False
    print(True)
    return True


def max(input: list[int]) -> int:
    """Function that results in maximum value from list."""
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    i: int = 0
    max = input[0]
    while i < len(input):
        if input[i] > max:
            max = input[i]
            i += 1
        else:
            i += 1
    print(max)
    return max


def is_equal(list1: list[int], list2: list[int]) -> bool:
    """Function checks if first list is equal to second list."""
    if len(list1) != len(list2):
        return False
    i: int = 0
    while i < len(list1) and len(list2):
        if list1[i] == list2[i]:
            i += 1
        else:
            print(False)
            return False
    print(True)
    return True


if __name__ == "__main__":
    is_equal([1, 0, 1], [2, 0, 1, 1, 2])