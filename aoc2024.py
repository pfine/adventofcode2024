import sys
from src.day01 import part_1, part_2

def read_input(input_file):
    with open(f"data/{input_file}", "r+") as dataFile:
        print(f"--- Reading inputfile: data/{input_file} --- ")
        print("Reading data from a file")
        return dataFile.readlines()

def runPart(day, part, input):
    print(f"Executing part {part}")
    print(f" >>> day = {day}")
    print(f" >>> part = {part}")
    print(f" >>> input = {input}")

    part_1(input) if part == 1 else part_2(input)


def main(argv):
    print(f" >>> argv = {argv}")
    input = read_input(argv[1])
    print(f" >>> input = {input}")

    runPart(argv[0], 1, input)
    runPart(argv[0], 2, input)

if __name__ == "__main__":
    print(f" >>> sys.argv = {sys.argv}")
    main(sys.argv[1:])

# python aoc2024.py 00 input_day01_1_example
