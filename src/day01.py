


def part_1(input_data: list[str]) -> None:
    """Function printing python version."""
    matrix = [[], []]
    lines = input_data
    lines = [line.strip() for line in lines]
    print("Lines = ", lines)

    for line in lines:
        print(" > line =", line)
        row = line.split()
        print(" > row =", row)
        matrix[0].append(int(row[0])) # convert to int
        matrix[1].append(int(row[1])) # convert to int

    print(f"matrix = {matrix}")

    # sort from lowest
    list_1 = matrix[0]
    print(" > list_1 =", list_1)
    list_1.sort() # sort in plase, result None
    print(" > list_1 =", list_1)
    # print(" > list_1 =", list_1, type(list_1), list_1.sort(reverse=False), list_1, sorted(list_1))
    list_2 = matrix[1]
    print(" > list_2 =", list_2)
    list_2.sort() # sort in place, result None
    print(" > list_2 =", list_2)
    # print(" > list_2 =", list_2, type(list_2), list_2.sort(reverse=False), list_2, sorted(list_2))

    print("matrix =", matrix)

    distance = 0
    # mesure distance
    for i in range(len(matrix[0])):
        distance = distance + abs(matrix[0][i] - matrix[1][i])
        print('   > summed distance between', matrix[0][i], "and", matrix[1][i], "is", abs(matrix[0][i] - matrix[1][i]))

    print(f"Summed distance is: {distance}")

def part_2(input_data: list[str]) -> None:
    """Function printing python version."""
    matrix = [[], []]
    lines = input_data
    lines = [line.strip() for line in lines]
    print("Lines = ", lines)

    for line in lines:
        print(" > line =", line)
        row = line.split()
        print(" > row =", row)
        matrix[0].append(int(row[0])) # convert to int
        matrix[1].append(int(row[1])) # convert to int

    print("matrix =", matrix)

    score = 0
    # mesure distance
    for i in range(len(matrix[0])):
        occurres_in_list2_times = matrix[1].count(matrix[0][i])
        score = score + matrix[0][i] * occurres_in_list2_times
        # print('   > Similarity score between element ', matrix[0][i], "and", matrix[1], "is", matrix[0][i] * occurres_in_list2_times)

    print(f'Similarity score is: {score}')
