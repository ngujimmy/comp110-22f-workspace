"""Tests util functions!"""

__author__ = "730574005"


from exercises.ex05.utils import only_evens, concat, sub


def test_only_evens_empty() -> None:
    """Tests an empty list."""
    evens: list[int] = []
    assert only_evens(evens) == []


def test_only_evens_three() -> None:
    """Tests a list with three integers."""
    evens: list[int] = [1, 2, 3]
    assert only_evens(evens) == [2]


def test_only_evens_five() -> None:
    """Tests a list with five integers."""
    evens: list[int] = [1, 2, 3, 4, 5]
    assert only_evens(evens) == [2, 4]


def test_concat_empty() -> None:
    """Tests the concat function on empty lists."""
    list1: list[int] = []
    list2: list[int] = []
    assert concat(list1, list2) == []


def test_concat_three_integers() -> None:
    """Tests the concat function using three integers."""
    list1: list[int] = [1, 2, 3]
    list2: list[int] = [3, 2, 1]
    assert concat(list1, list2) == [1, 2, 3, 3, 2, 1]



def test_concat_negative_integers() -> None:
    """Tests the concat function using three integers."""
    list1: list[int] = [-3, -1, -2]
    list2: list[int] = [-2, -1, -3]
    assert concat(list1, list2) == [-3, -1, -2, -2, -1, -3]


def test_sub_empty() -> None:
    """Tests the sub function when the end index is 0."""
    list: list[int] = [1, 2, 3]
    start: int = 1
    end: int = 0
    assert sub(list, start, end) == []


def test_sub_two_int() -> None:
    """Tests the sub function with a length of two."""
    list: list[int] = [1, 2, 3]
    start: int = 0
    end: int = 2
    assert sub(list, start, end) == [1, 2]


def test_sub_negative() -> None:
    """Tests the sub function when the start is negative."""
    list: list[int] = [1, 2, 3]
    start: int = -1
    end: int = 3
    assert sub(list, start, end) == [1, 2, 3]