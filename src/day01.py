
"""Module providing a function printing python version."""

def extract_data(input_data: list[str]) -> tuple[list[int], list[int]]:
    """Function printing python version."""
    # extract and transform data
    data1 = []
    data2 = []
    for l in input_data:
        x = l.split()
        data1.append(int(x[0]))
        data2.append(int(x[1]))

    return data1, data2

def part_1(input_data: list[str]) -> None:
    """Function printing python version."""
    data1, data2 = extract_data(input_data)

    # sort both lists asc
    data1.sort()
    data2.sort()

    # calculate absolute distance and add to sum
    sum_distance = 0
    # for i in range(0, len(data1)):
    #     sum_distance += abs(data1[i] - data2[i])
    for i, d1 in enumerate(data1):
        print(f" >>> iter: {i}, d1: {d1}")
        sum_distance += abs(d1 - data2[i])

    print(f"Solved 1: {sum_distance}")

def part_2(input_data: list[str]) -> None:
    """Function printing python version."""
    data1, data2 = extract_data(input_data)

    score = 0
    # mesure distance
    # for i in range(len(data1)):
    #     occurres_in_list2_times = data2.count(data1[i])
    #     score = score + data1[i] * occurres_in_list2_times
    #     print("   > Similarity score between element ", matrix[0][i], "and", matrix[1], "is", matrix[0][i] * occurres_in_list2_times)
    for i, d1 in enumerate(data1):
        print(f" >>> iter: {i}, d1: {d1}")
        occurres_in_list2_times = data2.count(d1)
        score = score + d1 * occurres_in_list2_times
        print(f"   > Similarity score between element {d1} and {data2} is {d1 * occurres_in_list2_times}")

    print(f'Similarity score is: {score}')
