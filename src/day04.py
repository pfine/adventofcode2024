
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

def path_right(data: list[list], i: int, j: int) -> bool: # direction: right -
    """Function for extracting data"""
    if len(data[i]) - j > 3:
        word = [data[i][j], data[i][j+1], data[i][j+2], data[i][j+3]]
        print(f" >>>-path1-> word = {word} or {"".join(word)}")
        if "".join(word) in ("XMAS", "SAMX"):
            return True
    return False

def path_down_right(data: list[list], i: int, j: int) -> bool: # direction: down right \
    """Function for extracting data"""
    if (len(data[i]) - j > 3) and (len(data) - i > 3):
        word = [data[i][j], data[i+1][j+1], data[i+2][j+2], data[i+3][j+3]]
        print(f" >>>-path1-> word = {word} or {"".join(word)}")
        if "".join(word) in ("XMAS", "SAMX"):
            return True
    return False

def path_down(data: list[list], i: int, j: int) -> bool: # direction: down |
    """Function for extracting data"""
    if len(data) - i > 3:
        word = [data[i][j], data[i+1][j], data[i+2][j], data[i+3][j]]
        print(f" >>>-path1-> word = {word} or {"".join(word)}")
        if "".join(word) in ("XMAS", "SAMX"):
            return True
    return False

def path_down_back_left(data: list[list], i: int, j: int) -> bool: # direction: down back left /
    """Function for extracting data"""
    if (j > 2) and (len(data) - i > 3):
        word = [data[i][j], data[i+1][j-1], data[i+2][j-2], data[i+3][j-3]]
        print(f" >>>-path1-> word = {word} or {"".join(word)}")
        if "".join(word) in ("XMAS", "SAMX"):
            return True
    return False

def find_mas_or_sam(elem1: str, elem2: str, elem3: str) -> bool: # search for MAS or SAM
    """Function for extracting data"""
    print(f" >>>-find_mas_or_sam-> checking for: {"".join([elem1, elem2, elem3])}")
    if "".join([elem1, elem2, elem3]) in ("MAS", "SAM"):
        return True
    return False

def find_x_mas_stamp(data: list[list], i: int, j: int) -> bool: # must be X with MAS or SAM
    """Function for extracting data"""
    if (len(data[i]) - j < 3) or (len(data) - i < 3):
        return False
    # check \ - [i][j], [i+1][j+1], [i+2][j+2]
    checking_down_right = find_mas_or_sam(data[i][j], data[i+1][j+1], data[i+2][j+2])
    # check / - [i+2][j], [i+1][j+1], [i][j+2]
    checking_up_right = find_mas_or_sam(data[i+2][j], data[i+1][j+1], data[i][j+2])
    # validation:
    if checking_down_right and checking_up_right:
        print(f" >>>-find_x_mas_stamp-> found XMAS stamp: [{i}][{j}]")
        return True
    return False

def print_matrix(matrix: list[list]) -> str:
    """Function for extracting data"""
    for _, row in enumerate(matrix):
        print("".join(row))

def part_1(input_data: list[str]) -> None:
    """Function part 1"""
    print(f" input_data = {input_data}")
    data = extract_data(input_data)
    print(f" data = {data}")

    print("\ndata:")
    print_matrix(data)

    # print("\nresult_matrix:")
    result_matrix = []
    for i, row in enumerate(data):
        result_matrix.append(["."] * len(row))
    # print_matrix(result_matrix)

    counted_true = 0
    # working or rows
    for i, row in enumerate(data):
        print(f"\niter: {i}, row: {row}")
        # result_matrix.append(["."] * len(row))
        for j, _ in enumerate(row):
            print(f" starting from line: {i}, column: {j} element: {row[j]}")
            # path_right
            if path_right(data, i, j):
                print(f"  - right: True <-------------- {counted_true}")
                result_matrix[i][j] = row[j]
                # word = [data[i][j], data[i][j+1], data[i][j+2], data[i][j+3]]
                result_matrix[i][j+1] = data[i][j+1]
                result_matrix[i][j+2] = data[i][j+2]
                result_matrix[i][j+3] = data[i][j+3]
                counted_true += 1
            # else:
            #     print("  - right: False")
            # path_down_right
            if path_down_right(data, i, j):
                print(f"  - down_right: True <-------------- {counted_true}")
                result_matrix[i][j] = row[j]
                # word = [data[i][j], data[i+1][j+1], data[i+2][j+2], data[i+3][j+3]]
                result_matrix[i+1][j+1] = data[i+1][j+1]
                result_matrix[i+2][j+2] = data[i+2][j+2]
                result_matrix[i+3][j+3] = data[i+3][j+3]
                counted_true += 1
            # else:
            #     print("  - down_right: False")
            # path_down
            if path_down(data, i, j):
                print(f"  - down: True <-------------- {counted_true}")
                result_matrix[i][j] = row[j]
                # word = [data[i][j], data[i+1][j], data[i+2][j], data[i+3][j]]
                result_matrix[i+1][j] = data[i+1][j]
                result_matrix[i+2][j] = data[i+2][j]
                result_matrix[i+3][j] = data[i+3][j]
                counted_true += 1
            # else:
            #     print("  - down: False")
            # path_down_back_left
            if path_down_back_left(data, i, j):
                print(f"  - down_back_left: True <-------------- {counted_true}")
                result_matrix[i][j] = row[j]
                # word = [data[i][j], data[i+1][j-1], data[i+2][j-2], data[i+3][j-3]]
                result_matrix[i+1][j-1] = data[i+1][j-1]
                result_matrix[i+2][j-2] = data[i+2][j-2]
                result_matrix[i+3][j-3] = data[i+3][j-3]
                counted_true += 1
            # else:
            #     print("  - down_back_left: False")

    print("\ndata:")
    print_matrix(data)

    print("\nresult_matrix:")
    print_matrix(result_matrix)

    print(f"\nSolved 1: XMAS occurs a total of: {counted_true}\n")

def part_2(input_data: list[str]) -> None:
    """Function part 2"""
    print(f" input_data = {input_data}")
    data = extract_data(input_data)
    print(f" data = {data}")

    print("\ndata:")
    print_matrix(data)

    # print("\nresult_matrix:")
    result_matrix = []
    for i, row in enumerate(data):
        result_matrix.append(["."] * len(row))
    # print_matrix(result_matrix)

    counted_true = 0
    # working or rows
    for i, row in enumerate(data):
        print(f"\niter: {i}, row: {row}")
        # result_matrix.append(["."] * len(row))
        for j, _ in enumerate(row):
            print(f" starting from line: {i}, column: {j} element: {row[j]}")
            # find_x_mas_stamp
            if find_x_mas_stamp(data, i, j):
                print(f"  - find_x_mas_stamp: True <-------------- {counted_true}")
                result_matrix[i][j] = row[j]
                # adding \ - data[i][j], data[i+1][j+1], data[i+2][j+2]
                result_matrix[i+1][j+1] = data[i+1][j+1]
                result_matrix[i+2][j+2] = data[i+2][j+2]
                # adding / - data[i+2][j], data[i+1][j+1], data[i][j+2]
                result_matrix[i+2][j] = data[i+2][j]
                result_matrix[i][j+2] = data[i][j+2]
                counted_true += 1
            # else:
            #     print("  - down_back_left: False")

    print("\ndata:")
    print_matrix(data)

    print("\nresult_matrix:")
    print_matrix(result_matrix)

    print(f"\nSolved 2: X-MAS occurs a total of: {counted_true}\n")
