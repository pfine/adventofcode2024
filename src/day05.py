
"""Module providing a function printing python version."""

def extract_data(input_data: list[str]) -> list[list]:
    """Function for extracting data"""
    # extract and transform data
    data = []
    for line in input_data:
        # print(f" line = {line}")
        row = list(map(int,line.split())) # convert row from str to int
        # print(f" row = {row}")
        data.append(row)
    # print(f" data = {data}")

    return data

def part_1(input_data: list[str]) -> None:
    """Function part 1"""
    print(f" input_data = {input_data}")
    data = extract_data(input_data)
    print(f" data = {data}")

    counted_sum = 0
    # working or rows
    for i, row in enumerate(data):
        print(f"\n iter: {i}, row: {row}")

    print(f"\nSolved 1: Number of safe reports are: {counted_sum}\n")


def part_2(input_data: list[str]) -> None:
    """Function part 2"""
    print(f" input_data = {input_data}")
    data = extract_data(input_data)
    print(f" data = {data}")

    counted_sum = 0
    # working or rows
    for i, row in enumerate(data):
        print(f"\n iter: {i}, row: {row}")

    print(f"\nSolved 2: Number of safe reports are: {counted_sum}\n")
