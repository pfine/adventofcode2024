def read_fine(path2file):
    with open(path2file, 'r', encoding="utf8") as file:
        lines = file.readlines()
    return lines

def process_line(line):
    pass

def main():
    path2file = './input/input_day01example'
    lines = read_fine(path2file)
    lines = [line.strip() for line in lines]
    print("Lines = ", lines)

    for line in lines:
        print(" > line = ", line)
        # processed_line = process_line(line)

    print("Hello World!")

if __name__ == "__main__":
    main()
