"""Tests dictionary functions!"""

__author__ = "730574005"


from exercises.ex07.dictionary import invert, favorite_color, count


def test_invert_empty() -> None:
    """Tests an empty dict."""
    test_dict: dict[str, str] = {}
    assert invert(test_dict) == {}


def test_invert_two_answers() -> None:
    """Tests invert with two answers."""
    test_dict: dict[str, str] = {'a': 'b', 'c': 'd'}
    assert invert(test_dict) == {'b': 'a', 'd': 'c'}


def test_invert_three_answers() -> None:
    """Tests invert with three answers."""
    test_dict: dict[str, str] = {'a': 'b', 'c': 'd', 'e': 'f'}
    assert invert(test_dict) == {'b': 'a', 'd': 'c', 'f': 'e'}


def test_favorite_color_none() -> None:
    """Tests favorite color no answers."""
    test_dict: dict[str, str] = {}
    assert favorite_color(test_dict) == ""


def test_favorite_color_blue() -> None:
    """Tests favorite color as blue."""
    test_dict: dict[str, str] = {'Jimmy': 'blue', 'Romi': 'blue', 'Stephen': 'green'}
    assert favorite_color(test_dict) == "blue"


def test_favorite_color_green() -> None:
    """Tests favorite color as green."""
    test_dict: dict[str, str] = {'Jimmy': 'blue', 'Romi': 'green', 'Stephen': 'green'}
    assert favorite_color(test_dict) == "green"


def test_count_empty() -> None:
    """Test count function with no answer."""
    test_list: list[str] = []
    assert count(test_list) == {}


def test_count_two_terms() -> None:
    """Test count function with two keys."""
    test_list: list[str] = ["red", "blue", "red"]
    assert count(test_list) == {'red': 2, 'blue': 1}


def test_count_three_terms() -> None:
    """Test count function with three keys."""
    test_list: list[str] = ["red", "blue", "red", "green", "blue"]
    assert count(test_list) == {'red': 2, 'blue': 2, 'green': 1}