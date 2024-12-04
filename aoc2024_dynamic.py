"""Module providing a function printing python version."""

import sys

def read_input(input_file: list[str]) -> list[str]:
    """Function printing python version."""
    with open(f"data/{input_file}", "r+", encoding="utf-8") as data_file:
        print(f"--- Reading from location: data/{input_file} --- ")
        print("Reading data from a file")
        return data_file.readlines()

def runPart(day, part, input_data) -> None:
    """Function printing python version."""
    print(f"Executing part {part}")
    # print(f" >>> day = {day}")
    # print(f" >>> part = {part}")
    # print(f" >>> input_data = {input_data}")

    fnc_part_one = 'part_1'
    fnc_part_two = 'part_2'
    importlib = __import__('importlib')
    mod = importlib.import_module(f"src.day{day}")

    func_one = getattr(mod, fnc_part_one)
    func_two = getattr(mod, fnc_part_two)

    func_one(input_data) if part == 1 else func_two(input_data)


def main(argv):
    """Function printing python version."""
    print(f"--- DAY {argv[0]} --- ")
    # print(f" >>> argv = {argv}")
    input_data = read_input(argv[1])
    # print(f" >>> input = {input}")

    runPart(argv[0], 1, input_data)
    runPart(argv[0], 2, input_data)

if __name__ == "__main__":
    print(f" >>> sys.argv = {sys.argv}")
    main(sys.argv[1:])

# Exec:
# python aoc2024_dynamic.py 02 input_day02_1_example
