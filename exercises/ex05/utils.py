"""Multiple new util functions!"""

__author__ = "730574005"


def only_evens(list1: list[int]) -> list[int]:
    """Computes list."""
    list2: list[int] = []
    for item in list1:
        if item % 2 == 0:
            list2.append(item)
    return list2


def concat(list1: list[int], list2: list[int]) -> list[int]:
    """Concatenates list."""
    full_list: list[int] = []
    for item in list1:
        full_list.append(item)
    for item in list2:
        full_list.append(item)
    return full_list


def sub(list: list[int], start: int, end: int) -> list[int]:
    """Creates a sub list between a start and end."""
    final_list: list[int] = []
    if len(list) == 0 or start >= len(list) or end <= 0:
        return final_list
    else:
        start_index: int = start
        max_index: int = end
        if start_index < 0:
            start_index = 0
        if max_index > len(list):
            max_index = len(list)
        while start_index < max_index:
            final_list.append(list[start_index])
            start_index += 1
    return final_list