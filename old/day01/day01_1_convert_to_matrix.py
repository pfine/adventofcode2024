def read_fine(path2file):
    with open(path2file, 'r', encoding="utf8") as file:
        lines = file.readlines()
    return lines

def print_matrix(matrix):
    for row in matrix:
        print(' '.join(str(row)))

def process_line(line):
    pass

def main():
    matrix = []
    path2file = './input/input_day01_1_example'
    lines = read_fine(path2file)
    lines = [line.strip() for line in lines]
    print("Lines = ", lines)

    for line in lines:
        print(" > line = ", line)
        # processed_line = process_line(line)
        row = list(map(int, line.split()))
        matrix.append(row)

    print('Result matrix =\n', print_matrix(matrix))

if __name__ == "__main__":
    main()
