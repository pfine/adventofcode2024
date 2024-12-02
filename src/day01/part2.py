def read_fine(path2file):
    with open(path2file, 'r', encoding="utf8") as file:
        lines = file.readlines()
    return lines

def process_line(line):
    pass

def main():
    matrix = [[], []]
    path2file = './input/input_day01_2'
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

    score = 0
    # mesure distance
    for i in range(len(matrix[0])):
        occurres_in_list2_times = matrix[1].count(matrix[0][i])
        score = score + matrix[0][i] * occurres_in_list2_times
        # print('   > Similarity score between element ', matrix[0][i], "and", matrix[1], "is", matrix[0][i] * occurres_in_list2_times)

    print('Similarity score is', score)


if __name__ == "__main__":
    main()
