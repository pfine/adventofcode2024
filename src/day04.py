
"""Module providing a function printing python version."""

def extract_data(input_data: list[str]) -> list[list]:
    """Function for extracting data"""
    # extract and transform data
    data = []
    for line in input_data:
        # print(f" line = {line}")
        row = list(line.rstrip()) # remove new line and convert to list
        # print(f" row = {row}")
        data.append(row)
    # print(f" data = {data}")

    return data

def path1(data: list[list], i: int, j: int) -> bool: # direction: right -
    """Function for extracting data"""
    word = str([data[i][j], data[i+1][j], data[i+2][j], data[i+3][j]])
    print(f" >>>-path1-> word = {word}")

    return True

def path2(data: list[list], i: int, j: int) -> bool: # direction: down right \
    """Function for extracting data"""
    pass

def path3(data: list[list], i: int, j: int) -> bool: # direction: down |
    """Function for extracting data"""
    pass

def path4(data: list[list], i: int, j: int) -> bool: # direction: down back left /
    """Function for extracting data"""
    pass

def part_1(input_data: list[str]) -> None:
    """Function part 1"""
    print(f" input_data = {input_data}")
    data = extract_data(input_data)
    print(f" data = {data}")

    counted_sum = 0
    # working or rows
    for i, row in enumerate(data):
        print(f"iter: {i}, row: {row}")

    print(f"\nSolved 1: XMAS occurs a total of: {counted_sum}\n")


def part_2(input_data: list[str]) -> None:
    """Function part 2"""
    print(f" input_data = {input_data}")
    data = extract_data(input_data)
    print(f" data = {data}")

    counted_sum = 0
    # working or rows
    for i, row in enumerate(data):
        print(f"iter: {i}, row: {row}")

    print(f"\nSolved 2: XMAS occurs a total of: {counted_sum}\n")
