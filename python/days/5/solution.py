def read_file(filename):
    data = open(filename).read().splitlines()

    seeds = [int(v) for v in data.pop(0).split(': ')[1].split()]
    
    maps = {}

    for line in data:
        if not line:
            continue

        if line.endswith(':'):
            src, dst = line.split()[0].split('-to-')
            maps[src] = {
                'dst': dst,
                'map': [] 
            }
        else:
            dst_start, src_start, length = line.split()
            maps[src]['map'].append({
                'dst_start': int(dst_start),
                'src_start': int(src_start),
                'length': int(length)
            })

    return seeds, maps

def recursively_map(val, cat, maps):
    print(f"trying to map {val} {cat}")
    if cat in maps:
        dst_type = maps[cat]['dst']

        for m in maps[cat]['map']:
            if val in range(m['src_start'], m['src_start']+m['length']+1):
                offset = val - m['src_start']
                return recursively_map(m['dst_start'] + offset, dst_type, maps)

        return recursively_map(val, dst_type, maps)

    return val, cat

def solve(filename, part2=False):
    values = []
    seeds, maps = read_file(filename)

    for seed in seeds:
        values.append(recursively_map(seed, 'seed', maps))

    return min(v[0] for v in values)

if __name__ == "__main__":
    print("Part 1 Test: ", solve('test_data.txt'))
    print("Part 1: ", solve('data.txt'))

    #print("Part 2 Test:", solve('test_data.txt', part2=True))
    #print("Part 2:", solve('data.txt', part2=True))