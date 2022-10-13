"""Trying out new functions using dictionaries."""

__author__ = "730574005"


from this import d


def invert(dict1: dict[str, str]) -> dict[str, str]:
    """Inverses the dictionary."""
    inverse_dict: dict[str, str] = {}
    for key in dict1:
        if dict1[key] not in inverse_dict:
            inverse_dict[dict1[key]] = key
        else:
            raise KeyError("Has multiple keys.")
    return inverse_dict


def count(list: list[str]) -> dict[str, int]:
    """Take count of number of values."""
    empty_dict: dict[str, int] = {}
    for item in list:
        if item in empty_dict:
            empty_dict[item] += 1
        else:
            empty_dict[item] = 1
    return empty_dict


def favorite_color(dict: dict[str, str]) -> str:
    """Shows most frequent color in dictionary."""
    frequent: list = []
    colors: dict[str, str] = dict
    new_dict = {}
    max_num = 0
    max_color = ""
    for key in colors:
        frequent.append(colors[key])
    new_dict = count(frequent)
    for key in new_dict:
        if new_dict[key] > max_num:
            max_num = new_dict[key]
            max_color = key
    return max_color