import sys
from src.day01 import part_1, part_2

def read_input(input_file):
    with open(f"data/{input_file}", "r+", encoding="utf-8") as dataFile:
        print(f"--- Reading inputfile: data/{input_file} --- ")
        print("Reading data from a file")
        return dataFile.readlines()

def run_part(day, part, input_data):
    print(f"Executing part {part}")
    print(f" >>> day = {day}")
    print(f" >>> part = {part}")
    print(f" >>> input_data = {input_data}")

    part_1(input_data) if part == 1 else part_2(input_data)


def main(argv):
    print(f" >>> argv = {argv}")
    input_data = read_input(argv[1])
    print(f" >>> input_data = {input_data}")

    run_part(argv[0], 1, input_data)
    run_part(argv[0], 2, input_data)

if __name__ == "__main__":
    print(f" >>> sys.argv = {sys.argv}")
    main(sys.argv[1:])

# python aoc2024.py 00 input_day01_1_example
