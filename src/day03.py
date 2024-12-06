"""Module providing a function printing python version."""

import re

def extract_data(input_data: list[str]) -> str:
    """Function for extracting data"""
    # extract and transform data
    data = map(lambda line: line.rstrip(), input_data)
    result = "".join(data)
    print(f" >>> result = {result}")

    return result


def part_1(input_data: list[str]) -> None:
    """Function part 1"""
    print(f" input_data = {input_data}")
    data = extract_data(input_data)
    print(f" data = {data}")

    counted_sum = 0
    # working with whole text
    # (mul\([0-9]{1,3},[0-9]{1,3}\))
    find_mul = re.findall(r'mul\(\d{1,3},\d{1,3}\)', data) # collect list: ['mul(2,4)', 'mul(5,5)', 'mul(11,8)', 'mul(8,5)']
    print(find_mul)
    for i, mul in enumerate(find_mul):
        print(f" >>> iter: {i}, mul: {mul}")
        calculate_this=re.findall(r'\d{1,3},\d{1,3}', mul) # collect list: ['2,4']
        print(f" >>>--> calculate_this = {calculate_this}")
        split_mul=calculate_this[0].split(',') # collect list: ['2', '4']
        print(f" >>>--> split_mul = {split_mul}")
        counted_sum = counted_sum + int(split_mul[0]) * int(split_mul[1]) # 2 * 4

    print(f"\nSolved 1: Total sum is: {counted_sum}\n")


def part_2(input_data: list[str]) -> None:
    """Function part 2"""
    print(f" input_data = {input_data}")
    data = extract_data(input_data)
    print(f" data = {data}")

    counted_sum = 0
    # working or rows


    print(f"\nSolved 2:Total sum (including do / dont's) is: {counted_sum}\n")
