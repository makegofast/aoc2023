def read_file(filename):
    cards = {}
    for line in open(filename).read().splitlines():
        card_no, line = line.split(': ')
        card_no = int(card_no.split()[1])

        winners, numbers = line.split(' | ')
        winners = winners.split()
        numbers = numbers.split()

        cards[card_no] = {
            'winners': [int(n) for n in winners],
            'numbers': [int(n) for n in numbers]
        }
    
    return cards 

def score_card(card):
    num_count = [n for n in card['numbers'] if n in card['winners']]

    return len(num_count), int(2**(len(num_count)-1))

def solve(filename, part2=False):
    cards = read_file(filename)

    total = {}

    for i in range(1, len(cards)+1):
        total[i] = {
            'copies': 1, 
            'points': 0
        }

    for card_no, card in cards.items():
        winners, points = score_card(card)

        total[card_no]['points'] = points 
        
        for i in range(card_no+1, card_no+winners+1):
            if i in total:
                total[i]['copies'] += total[card_no]['copies']
        
    if part2:
        return sum([c['copies'] for i, c in total.items()])
    else:
        return sum([c['points'] for i, c in total.items()])

    return total

if __name__ == "__main__":
    print("Part 1 Test: ", solve('test_data.txt'))
    print("Part 1: ", solve('data.txt'))

    print("Part 2 Test:", solve('test_data.txt', part2=True))
    print("Part 2:", solve('data.txt', part2=True))