import math
from colorama import Fore, Style

d_up, d_down, d_left, d_right = (-1, 0), (1, 0), (0, -1), (0, 1)
d_all = [d_up, d_down, d_left, d_right]
dir_map = { #change in row, change in col sets
    'J': [ d_left, d_up ],
    '7': [ d_left, d_down ],
    'F': [ d_right, d_down ],
    'L': [ d_up, d_right ],
    '|': [ d_up, d_down ],
    '-': [ d_left, d_right ],
    '.': []
}

map = []
start = None
outside = []

def in_bounds(pos):
    global map

    #print(f"in_bounds check of {pos}")
    row, col = pos[0], pos[1]

    if row >= 0 \
        and row < len(map) \
        and col >= 0 \
        and col < len(map[row]):
        #print(f"{pos} is in bounds")
        return True
    else:
        #print(f"{pos} is OUT of bounds")
        return False

def read_file(filename, part2=False):
    map = []
    start = None
    for row, line in enumerate(open(filename).read().splitlines()):
        if 'S' in line:
            start = [row, line.index('S')]
        map.append([c for c in line])

    return map, start

def print_map(start, visited, enclosed, max_rows=None):
    global map, outside

    print(Style.RESET_ALL)
    for row, line in enumerate(map):
        if max_rows and row > max_rows:
            break
        for col, c in enumerate(line):
            if [row, col] == start:
                color = Fore.MAGENTA + Style.BRIGHT
            elif [row, col] in visited:
                color = Fore.BLUE + Style.BRIGHT
            elif [row, col] in enclosed:
                color = Fore.RED + Style.BRIGHT
            elif [row, col] in outside:
                color = Fore.GREEN + Style.DIM
            else:
                color = Fore.WHITE + Style.DIM

            print(color + c, end="")
        print()
    print(Style.RESET_ALL)

def find_incoming(pos):
    global d_all

    incoming = []
    #print(f"Testing for incoming nodes to {pos}")
    for d in d_all:
        t = [pos[0] + d[0], pos[1] + d[1]] 
        tn = find_next(t, [])
        if in_bounds(t) and pos in tn: 
            #print(f"{t} does connect to {pos} tn={tn}")
            incoming.append(t)
        else:
            #print(f"{t} does NOT connect to {pos} tn={tn}")
            pass
    
    #print(f"locations incoming to {pos}: {incoming}")
    return incoming

def find_next(pos, visited):
    global d_all, map

    #print("find_next checking", pos, "visited", visited)

    if not in_bounds(pos):
        return None 

    pos_r, pos_c = pos
    c = map[pos_r][pos_c]

    ret = []
    for dr, dc in dir_map[c]:
        t = [pos_r + dr, pos_c + dc]
        if in_bounds(t) and t not in visited:
            ret.append(t)
    
    return ret 

def check_for_enclosed_tiles(visited, max_rows=None):
    global map, outside

    enclosed = []

    loop_states = "O" * len(map[0])
    for row, line in enumerate(map):
        if max_rows and row > max_rows:
            break

        for col, c in enumerate(line):
            if c in ["F"]:
                loop_states[col] = "I"
            elif c in ["7"]:
                loop_states[col] = "O"
            elif c in ["|"]:
                inside_loop = not inside_loop 

            if inside_loop: 
                enclosed.append([row, col])
            else:
                outside.append([row, col])

    print("enclosed:", '\n'.join([str(v) for v in enclosed]))

    return enclosed

def solve(filename, part2=False):
    global map, start, outside
    visited = [] 

    map, start = read_file(filename, part2)

    n = find_incoming(start)[0]
    visited.append(start)

    steps = 0
    while n:
        #print(f"n = {n}")
        visited.append(n)

        n = find_next(n, visited)

        if len(n):
            n = n[0]
        
        steps += 1

    print_map(start, visited, [], max_rows=20)

    enclosed = check_for_enclosed_tiles(visited, max_rows=20)

    print_map(start, visited, enclosed, max_rows=20)

    print(f"steps: {steps}")
    print(f"enclosed: {len(enclosed)}")
    return math.ceil(steps/2)

if __name__ == "__main__":
    print("Part 1 Test: ", solve('test_data.txt'))
    print("Part 1 Test 2: ", solve('test_data_2.txt'))
    print("Part 1 Test 3: ", solve('test_data_3.txt'))
    #print("Part 1: ", solve('data.txt'))

    #print("Part 2 Test:", solve('test_data.txt', part2=True))
    #print("Part 2:", solve('data.txt', part2=True))