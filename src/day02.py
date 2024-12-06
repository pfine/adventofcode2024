
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


def count_distance(row: list[int]) -> list[int]:
    """Function counting distance betwee array elements"""
    distance = []
    for i in range(len(row) - 1):
        dist = row[i + 1] - row[i]
        distance.append(dist)

    return distance

def check_safety(row: list[int]) -> tuple[bool, str]:
    """Function for checking safety"""
    distance = count_distance(row)
    print(f" >>>-check_safety-> distance = {distance}")

    check_if_in_range = all((abs(x) >= 1 and abs(x) <= 3) for x in distance)
    print(f" >>>-check_safety-> check_if_in_range = {check_if_in_range}")
    if not check_if_in_range:
        print(" >>>   - Unsafe (chaged too much, or not all)")
        return (False, "range")

    check_if_the_same_sign = all(x > 0 for x in distance) or all(x < 0 for x in distance)
    print(f" >>>-check_safety-> check_if_the_same_sign = {check_if_the_same_sign}")
    if not check_if_the_same_sign:
        print(" >>>   - Unsafe (chaged in sign)")
        return (False, "sign")

    print(" >>>   - Safe")
    return (True, "")

def check_safety_extended(row: list[int], fail_safty = False) -> bool:
    """Function for checking safety extended"""
    distance = count_distance(row)
    print(f" >>>-check_safety_extended-> distance = {distance}")

    if check_safety(row)[0]:
        print(" >>>   - Safe (already w/o any rlemnt removed)")
        return True

    # 

    check_if_in_range = any((abs(x) < 1 or abs(x) > 3) for x in distance)
    print(f" >>>-check_safety_extended-> check_if_in_range = {check_if_in_range}")
    if not check_if_in_range:
        print(" >>>   - Unsafe (chaged too much, or not all)")
        if fail_safty:
            # try with remove 1 element
            print(" >>>----> fail_safty procedure for RANGE")

        else:
            return False

    check_if_the_same_sign = all(x > 0 for x in distance) or all(x < 0 for x in distance)
    print(f" >>>-check_safety_extended-> check_if_the_same_sign = {check_if_the_same_sign}")
    if not check_if_the_same_sign:
        print(" >>>   - Unsafe (chaged in sign)")
        if fail_safty:
            # try with remove 1 element
            print(" >>>----> fail_safty procedure for SIGN")

        else:
            return False

    print(" >>>   - Safe")
    return True


def part_1(input_data: list[str]) -> None:
    """Function part 1"""
    print(f" input_data = {input_data}")
    data = extract_data(input_data)
    print(f" data = {data}")

    safe_count = 0
    # working or rows
    for i, row in enumerate(data):
        print(f"\n iter: {i}, row: {row}")
        if check_safety(row)[0]:
            safe_count += 1

    print(f"\nSolved 1: Number of safe reports are: {safe_count}\n")


def part_2(input_data: list[str]) -> None:
    """Function part 2"""
    print(f" input_data = {input_data}")
    data = extract_data(input_data)
    print(f" data = {data}")

    safe_count = 0
    # working or rows
    for i, row in enumerate(data):
        print(f"\n iter: {i}, row: {row}")
        if check_safety_extended(row, True):
            safe_count += 1
        else:
            print(f" - try with remove 1 level")

    print(f"\nSolved 2: Number of safe reports are: {safe_count}\n")
