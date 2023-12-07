import re

def read_file(filename):
    data = {}
    for line in open(filename).read().splitlines():
        game_no, game_data = line.split(": ")
        game_data = game_data.split("; ")

        game_no = int(game_no.replace('Game ', ''))
        data.setdefault(game_no, [])

        for sd in game_data:
            data[game_no].append(parse_set_data(sd))

    return data

def parse_set_data(set_data):
    ret = {'red': 0, 'green': 0, 'blue': 0}
    for count, color in [sd.split(' ') for sd in set_data.split(', ')]:
      ret[color] = int(count)
    
    return ret
   
def solve(filename, part2=False):
    data = read_file(filename)
    
    total = 0
    total_power = 0

    for game_no, game_data in data.items():
        impossible = any([True for sd in game_data if sd['red'] > 12 or sd['green'] > 13 or sd['blue'] > 14])
        if not impossible:
            total += game_no
        
        print(game_no, impossible)

        min_red = max([sd['red'] for sd in game_data])
        min_green = max([sd['green'] for sd in game_data])
        min_blue = max([sd['blue'] for sd in game_data])

        total_power += min_red * min_green * min_blue

        print(f"red {min_red} green {min_green} blue {min_blue}")

    return total_power if part2 else total

if __name__ == "__main__":
    print("Part 1 Test: ", solve('test_data.txt'))
    print("Part 1: ", solve('data.txt'))

    print("Part 2 Test:", solve('test_data.txt', part2=True))
    print("Part 2:", solve('data.txt', part2=True))