import math
galaxies = {}
row_expansion = {}
col_has_galaxies = {}

def read_file(filename):
    global galaxies, row_expansion, col_has_galaxies

    row_expansion = {}
    col_has_galaxies = {}

    gid = 0
    for row, line in enumerate(open(filename).read().splitlines()):
        if '#' not in line:
            row_expansion[row] = True 
        
        for col, c in enumerate(line):
            if c == "#":
                gid += 1
                col_has_galaxies[col] = True
                galaxies[gid] = [row, col]
    
def cal_distances(expansion_factor):
    global galaxies, col_has_galaxies
    seen = {}
    distances = []

    for sgid, sc in galaxies.items():
        #if sgid % 100 == 0:
        #    print(f"{sgid}/{len(galaxies)} {math.floor(sgid/len(galaxies)*100)}%")
        for dgid, dc in galaxies.items():
            if sgid == dgid:
                #print(f"skipping {sgid}->{dgid} as they are the same")
                continue
            
            if f"{dgid}->{sgid}" in seen:
                #print(f"skipping {sgid}->{dgid} as we've already seen the reverse {dgid}->{sgid}")
                continue

            rs = min(sc[0], dc[0])
            re = max(sc[0], dc[0])
            cs = min(sc[1], dc[1])
            ce = max(sc[1], dc[1])
            row_exp = sum([expansion_factor if i in row_expansion else 1 for i in range(rs, re)])
            col_exp = sum([expansion_factor if i not in col_has_galaxies else 1 for i in range(cs, ce)])
            d = row_exp + col_exp
            #print(f"cal {sgid}->{dgid} = {d} (sc={sc} dc={dc} rs={rs} re={re} cs={cs} ce={ce} row_exp={row_exp}, col_exp={col_exp})")
            distances.append(d)

            seen[f"{sgid}->{dgid}"] = True

    return sum(distances)
            
def print_map(map):
    print()
    for row, line in enumerate(map):
        for col, c in enumerate(line):
            print(c, end="")
        print()

def solve(filename, expansion_factor=1):
    global galaxies, row_expansion, col_has_galaxies
    galaxies = {}
    row_expansion = {}
    col_has_galaxies = {}

    read_file(filename)
    sum_d = cal_distances(expansion_factor)
    return sum_d


if __name__ == "__main__":
    print("Part 1 Test: ", solve('test_data.txt'))
    print("Part 1: ", solve('data.txt'))

    print("Part 2 Test (10):", solve('test_data.txt', 10))
    print("Part 2 Test (100):", solve('test_data.txt', 100))
    print("Part 2:", solve('data.txt', 1000000))