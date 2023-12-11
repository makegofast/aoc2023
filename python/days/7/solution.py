card_points = [
    '', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A'
]

def read_file(filename, part2=False):
    for line in open(filename).read().splitlines():
        yield line.split() 

def score_hand(hand):
    symbol_counts = {}
    for c in hand:
        symbol_counts[c] = symbol_counts.get(c, 0) + 1
    
    symbol_counts = {k: v for k, v in sorted(symbol_counts.items(), key=lambda x: x[1]-1)}

    base = max(symbol_counts.values()) * (5 - len(symbol_counts)) 
    sub = '.'.join([str(card_points.index(c)).rjust(2, '0') for i, c in enumerate(hand)])

    score = str(base).rjust(2, '0') + '.' + sub 
    #print(hand, symbol_counts, score)

    return score

def solve(filename, part2=False):
    data = read_file(filename, part2)

    data = sorted(data, key=lambda x: score_hand(x[0]))
    
    total = 0
    for i, d in enumerate(data):
        rank = i+1
        bid = d[1]
        winnings = int(bid)*rank
        print(rank, d, score_hand(d[0]), winnings)
        total += winnings

    return total

if __name__ == "__main__":
    print("Part 1 Test: ", solve('test_data.txt'))
    print("Part 1: ", solve('data.txt'))

    #print("Part 2 Test:", solve('test_data.txt', part2=True))
    #print("Part 2:", solve('data.txt', part2=True))