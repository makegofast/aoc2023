import math

def read_file(filename, part2=False):
    galaxies = []
    map = []

    col_data = {}
    for row, line in enumerate(open(filename).read().splitlines()):
        map.append([c for c in line])

        if '#' not in line:
            map.append(map[-1].copy())

        for col, cnt in {i: 1 for i, v in enumerate(map[-1]) if v=="#"}.items():
            col_data.setdefault(col, 0)
            col_data[col] += 1
    
    for i in range(len(map[-1])-1, 0, -1):
        if i not in col_data:
            for r, m in enumerate(map):
                map[r].insert(i, '.')

    for row, line in enumerate(map):
        for col, c in enumerate(line):
            if c == "#":
                galaxies.append([row, col])

    return map, galaxies
    
def cal_distances(map, galaxies):
    seen = {}
    distances = []

    for sgid, sc in enumerate(galaxies):
        if sgid % 10 == 0:
            print(f"{sgid}/{len(galaxies)} {math.floor(sgid/len(galaxies)*100)}%")
        for dgid, dc in enumerate(galaxies):
            if sgid == dgid:
                #print(f"skipping {sgid}->{dgid} as they are the same")
                continue
            
            if f"{dgid}->{sgid}" in seen:
                #print(f"skipping {sgid}->{dgid} as we've already seen the reverse {dgid}->{sgid}")
                continue

            d = abs(dc[0]-sc[0]) + abs(dc[1]-sc[1]) 
            #print(f"cal {sgid+1}->{dgid+1} = {d}")
            distances.append(d)

            seen[f"{sgid}->{dgid}"] = True

    print("sum:", sum(distances))
    return sum(distances)
            
def print_map(map):
    print()
    for row, line in enumerate(map):
        for col, c in enumerate(line):
            print(c, end="")
        print()

def solve(filename, part2=False):
    map, galaxies = read_file(filename, part2)
    sum_d = cal_distances(map, galaxies)
    return sum_d


if __name__ == "__main__":
    print("Part 1 Test: ", solve('test_data.txt'))
    print("Part 1: ", solve('data.txt'))

    #print("Part 2 Test:", solve('test_data.txt', part2=True))
    #print("Part 2:", solve('data.txt', part2=True))