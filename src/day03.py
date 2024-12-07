"""Module providing a function printing python version."""

import re

def extract_data(input_data: list[str]) -> str:
    """Function for extracting data"""
    # extract and transform data
    data = map(lambda line: line.rstrip(), input_data)
    result = "".join(data)
    print(f" >>> result = {result}")

    return result

def calculate_one_mul(mul_to_calc: str) -> int: # mul(2,4)
    """Function for extracting data"""
    mul_list=re.findall(r'\d{1,3},\d{1,3}', mul_to_calc) # collect list: ['2,4']
    print(f" >>>--> mul_list = {mul_list}")
    split_mul_list=mul_list[0].split(',') # collect list: ['2', '4']
    print(f" >>>--> split_mul = {split_mul_list}")
    result = int(split_mul_list[0]) * int(split_mul_list[1]) # 2 * 4

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
        counted_sum = counted_sum + calculate_one_mul(mul)

    print(f"\nSolved 1: Total sum is: {counted_sum}\n")


def part_2(input_data: list[str]) -> None:
    """Function part 2"""
    print(f" input_data = {input_data}")
    data = extract_data(input_data)
    print(f" data = {data}")

    counted_sum = 0
    # working with whole text
    # (don\'t\(\)|do\(\)|mul\([0-9]{1,3},[0-9]{1,3}\)
    find_mul = re.findall(r'(don\'t\(\)|do\(\)|mul\([0-9]{1,3},[0-9]{1,3}\))', data) # collect list: ['mul(2,4)', "don't()", 'mul(5,5)', 'mul(11,8)', 'do()', 'mul(8,5)']
    dont_enable=False # enable counting, disable by don't() keyword
    for i, mul in enumerate(find_mul):
        print(f" >>> iter: {i}, mul: {mul}")
        if mul == "don't()":
            dont_enable=True
            continue
        elif mul == "do()":
            dont_enable=False
            continue
        if not dont_enable:
            counted_sum = counted_sum + calculate_one_mul(mul)

    print(f"\nSolved 2:Total sum (including do / dont's) is: {counted_sum}\n")
