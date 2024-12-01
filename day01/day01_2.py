def read_fine(path2file):
    with open(path2file, 'r', encoding="utf8") as file:
        lines = file.readlines()
    return lines

def process_line(line):
    pass

def main():
    matrix = [[], []]
    path2file = './input/input_day01'
    lines = read_fine(path2file)
    lines = [line.strip() for line in lines]
    print("Lines = ", lines)

    for line in lines:
        print(" > line =", line)
        # processed_line = process_line(line)
        row = line.split()
        print(" > row =", row)
        matrix[0].append(int(row[0])) # convert to int
        matrix[1].append(int(row[1])) # convert to int

    print("matrix =", matrix)

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

    print('Summed distance is', distance)


if __name__ == "__main__":
    main()
