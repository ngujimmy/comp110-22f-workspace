"""Dictionary related utility functions."""

__author__ = "730574005"

# Define your functions below
from csv import DictReader


def read_csv_rows(filename) -> list[dict[str, str]]:
    """Read the rows of a csv into a 'table'."""
    result: list[dict[str, str]] = []
    #Open a handle to the data file
    file_handle = open(filename, "r", encoding="utf8")
    # Prepare to read the data file as a CSV rather than just strings
    csv_reader = DictReader(file_handle)
    # Read each row of the CSV line-by-line
    for row in csv_reader:
        result.append(row)
    # Close the file when we're done, to free its resources.
    file_handle.close()
    return result


def column_values(list_rows, column) -> list[str]:
    """Produce a list[str] for all values in a single column."""
    result: list[str] = []
    for row in list_rows:
        item: str = row[column]
        result.append(item)
    return result


def columnar(row_table) -> dict[str, list[str]]:
    """Transform a row-oriented table into a column-oritented table."""
    result: dict[str, list[str]] = {}
    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)
    return result


def head(column_table, rows) -> dict[str, list[str]]:
    """Producecs a new column-based table with only the first N amount of rows of data."""
    result: dict[str, list[str]] = {}
    for column in column_table:
        empty_list: list[str] = []
        for index in range(0, rows):
            empty_list.append(column_table[column][index])
        result[column] = empty_list
    return result


def select(column_table, columns) -> dict[str, list[str]]:
    result: dict[str, list[str]] = {}
    for column in columns:
        result[column] = column_table[column]
    return result


def concat(dict1, dict2) -> dict[str, list[str]]:
    result: dict[str, list[str]] = {}
    for column in dict1:
        result[column] = dict1[column]
    for column in dict2:
        if result[column]:
            result[column] += dict2[column]
        else:
            result[column] = dict2[column]
    return result


def count(list1) -> dict[str, int]:
    result: dict[str, int] = {}
    for item in list1:
        if item in result:
            result[item] += 1
        else:
            result[item] = 1
    return result