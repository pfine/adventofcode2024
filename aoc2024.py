import sys
from src import day00, day01, day02

def readInput(day):
    with open(f"data/day{day}.txt", "r+") as dataFile:
        print(f"--- DAY {day} --- ")
        print("Reading data from a file")
        return dataFile.readlines()

def runPart(day, part, input):
    print(f"Executing part {part}")

    match day:
        case "0":
            day00.executePartOne(input) if part == 1 else day00.executePartTwo(input)
        case "1":
            day01.executePartOne(input) if part == 1 else day01.executePartTwo(input)
        case "2":
            day02.executePartOne(input) if part == 1 else day02.executePartTwo(input)

def main(argv):
    input = readInput(argv[0])
    # print(data)

    runPart(argv[0], 1, input)
    runPart(argv[0], 2, input)

if __name__ == "__main__":
    main(sys.argv[1:])
