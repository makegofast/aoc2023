def read_file(filename):
    data = []
    number_map = {} 
    symbol_map = {}

    for row, line in enumerate(open(filename).read().splitlines()):
        data.append([c for c in line])
        number_map[row] = scan_row_for_numbers(line)
        symbol_map[row] = scan_row_for_symbols(line)
    
    return data, number_map, symbol_map

def scan_row_for_symbols(line):
    ranges = []
    for pos, c in enumerate(line):
        if not c.isnumeric() and c != '.':
            ranges.append({
                'pos': pos,
                'symbol': c
            })

    return ranges
            
def scan_row_for_numbers(line):
    ranges = [] 

    buf = ""
    start = None
    end = None

    for pos, c in enumerate(line):
        if c.isnumeric():
            if start is None:
                start = pos
            buf += c 

        if buf and (not c.isnumeric() or pos >= len(line)-1):
            end = pos - 1
            ranges.append({
                "start": start,
                "end": end,
                "value": int(buf)
            })

            start = None
            end = None
            buf = ""

    return ranges

def find_numbers_around(trow, tcol, number_map, data):
    matches = []
    for row in range(trow-1, trow+2):
        row_matches = [n['value'] for n in number_map[row] if abs(n['start']-tcol)<=1 or abs(n['end']-tcol)<=1]
        #print(f"row matches for {row} {trow-1}-{trow+2}: {row_matches}")
        matches += row_matches

    return matches

def solve(filename, part2=False):
    data, number_map, symbol_map = read_file(filename)
    part_numbers = []

    for row, locations in symbol_map.items():
        for location in locations:
            numbers = find_numbers_around(row, location['pos'], number_map, data)

            if part2:
                if location['symbol'] == "*" and len(numbers)==2:
                    part_numbers += [numbers[0] * numbers[1]]
            else:
                part_numbers += numbers 
    
    return sum(part_numbers)

if __name__ == "__main__":
    print("Part 1 Test: ", solve('test_data.txt'))
    print("Part 1: ", solve('data.txt'))

    print("Part 2 Test:", solve('test_data.txt', part2=True))
    print("Part 2:", solve('data.txt', part2=True))