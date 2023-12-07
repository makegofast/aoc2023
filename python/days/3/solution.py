def read_file(filename):
    data = []
    for line in open(filename).read().splitlines():
        data.append([c for c in line])
    
    return data

def symbols_around(row, col, data):
    coords = [
        (0, -1), #left
        (0, 1), #right
        (-1, 0), #above
        (1, 0), #below
        (-1, -1), #up-left
        (-1, 1), #up-right
        (1, -1), #down-left
        (1, 1) #down-right
    ]

    for drow, dcol in coords:
        trow, tcol = row+drow, col+dcol 

        try:
            c = data[trow][tcol] 
            if not c.isnumeric() and c != '.':
                return True
        except IndexError:
            pass

def solve(filename, part2=False):
    data = read_file(filename)
    part_numbers = []

    for row, line in enumerate(data):
        buf = ""
        valid = False
        for col, val in enumerate(line):
            if val.isnumeric():
                buf += val 
                if symbols_around(row, col, data):
                    valid = True
            
            if not val.isnumeric() or col == len(line)-1:
                if buf and valid:
                    part_numbers.append(int(buf))
                buf = ""
                valid = False

    print(part_numbers)
    return sum(part_numbers)


if __name__ == "__main__":
    print("Part 1 Test: ", solve('test_data.txt'))
    print("Part 1: ", solve('data.txt'))

    #print("Part 2 Test:", solve('test_data.txt', part2=True))
    #print("Part 2:", solve('data.txt', part2=True))