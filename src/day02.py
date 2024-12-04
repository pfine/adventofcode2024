
"""Module providing a function printing python version."""

def extract_data(input_data: list[str]) -> list[list]:
    """Function printing python version."""
    # extract and transform data
    data = []
    for line in input_data:
        # print(f" line = {line}")
        row = list(map(int,line.split())) # convert row from str to int
        # print(f" row = {row}")
        data.append(row)
    # print(f" data = {data}")

    return data


def check_if_all_the_same_sign(distance: list[int]) -> bool:
    """Function printing python version."""
    # print(f" >>--> check_if_all_the_same_sign - distance = {distance}")
    # print(f" >>--> all = {all(x > 0 for x in distance) or all(x < 0 for x in distance)}")
    return all(x > 0 for x in distance) or all(x < 0 for x in distance)


def check_safety(row: list[int]) -> bool:
    """Function printing python version."""
    distance = []
    for i in range(len(row) - 1):
        dist = row[i + 1] - row[i]
        if abs(dist) < 1 or abs(dist) > 3:
            print(f" >>>  For {i} - distance between {row[i + 1]} and {row[i]} = {dist}")
            print(" >>>   - Unsafe (chaged too much, or not all)")
            return False
        distance.append(dist)

    # print(f" >>> distance = {distance}")
    if not check_if_all_the_same_sign(distance):
        print(" >>>   - Unsafe (chaged in sign)")
        return False

    print(" >>>   - Safe")
    return True


def part_1(input_data: list[str]) -> None:
    """Function printing python version."""
    print(f" >>> input_data = {input_data}")
    data = extract_data(input_data)
    print(f" >>> data = {data}")

    safe_count = 0
    # working or rows
    for i, row in enumerate(data):
        print(f" >>> iter: {i}, row: {row}")
        if check_safety(row):
            safe_count += 1

    print(f"Solved 1: Number of safe reports are: {safe_count}")


def part_2(input_data: list[str]) -> None:
    """Function printing python version."""
    data = extract_data(input_data)

    score = 0
    # mesure distance
    # for i in range(len(data1)):
    #     occurres_in_list2_times = data2.count(data1[i])
    #     score = score + data1[i] * occurres_in_list2_times
    #     print("   > Similarity score between element ", matrix[0][i], "and", matrix[1], "is", matrix[0][i] * occurres_in_list2_times)
    # for i, d1 in enumerate(data1):
    #     print(f" >>> iter: {i}, d1: {d1}")
    #     occurres_in_list2_times = data2.count(d1)
    #     score = score + d1 * occurres_in_list2_times
    #     print(f"   > Similarity score between element {d1} and {data2} is {d1 * occurres_in_list2_times}")

    # print(f'Similarity score is: {score}')
