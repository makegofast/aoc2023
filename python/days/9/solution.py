def read_file(filename, part2=False):
    for line in open(filename).read().splitlines():
        yield [int(c) for c in line.split()]

def solve(filename, part2=False):
    data = read_file(filename, part2)
    last_values = []
    first_values = []

    for ds in data:
        history = [ds]

        while True:
            diffs = []
            for i in range(1, len(history[-1])):
                diffs.append(int(history[-1][i]) - int(history[-1][i-1]))
            
            #print(diffs)
            history.append(diffs)

            if not len([v for v in diffs if v != 0]):
                break
        
        history[-1] = [0] + history[-1] + [0]

        for hi in range(len(history)-1, 0, -1):
            ld = history[hi][-1]
            fd = history[hi][0]
            history[hi-1].append(history[hi-1][-1] + ld)
            history[hi-1].insert(0, history[hi-1][0] - fd)

        #print('history')
        #print('\n'.join([str(h) for h in history]))

        last_values.append(history[0][-1])
        first_values.append(history[0][0])

    #print('firsts', first_values, 'lasts', last_values)
    ret = sum(first_values) if part2 else sum(last_values)
    return ret 

if __name__ == "__main__":
    print("Part 1 Test: ", solve('test_data.txt'))
    print("Part 1: ", solve('data.txt'))

    print("Part 2 Test:", solve('test_data.txt', part2=True))
    print("Part 2:", solve('data.txt', part2=True))