"""EX04 List."""
__author__ = "730574005"


def all(int_list: list, test: int) -> bool:
    i: int = 0
    match: int = test
    result: bool = False 
    while i < len(int_list):
        if match == int_list[i]:
            result = True
            match = int_list[i]
            i += 1 
        else:
            result = False
            match = int_list[i]
            i += 1
    if result == True:
        print(True)
        return True
    else:
        print(False)
        return False


def max(int_list: list) -> int:
    i: int = 0
    max: int = int_list[0]
    while i > len(int_list):
        if int_list[i] > max:
            max = int_list[i]
            i += 1
        i += 1
    print(max)
    return(max)


