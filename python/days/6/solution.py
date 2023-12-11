def read_file(filename, part2=False):
    data = open(filename).read().splitlines()

    times = data[0].split(':')[1]
    distances = data[1].split(':')[1]

    if part2:
        times = times.replace(' ', '')
        distances = distances.replace(' ', '')

    print(times)
    print(distances)

    times = [int(v) for v in times.split()]
    distances = [int(v) for v in distances.split()]

    return zip(times, distances)

def solve(filename, part2=False):
    import math

    total = 0

    for record_time, distance in read_file(filename, part2):
        max_hold = min([distance-1, record_time-1])

        print(f"record time: {record_time}, distance: {distance}, max_hold: {max_hold}")

        ways_to_win = 0

        for hold_time in range(max_hold, 1, -1):
            speed = hold_time
            time_left = record_time-hold_time
            distance_travelled = speed*time_left
            if distance_travelled > distance:
                winner = True
                ways_to_win += 1
            else:
                winner = False

            if hold_time % 1000 == 0 or hold_time < 10:
                print(f" {speed} mm/s for {time_left} s = {distance_travelled} {winner} {hold_time}")
        
        total = ways_to_win * (total if total else 1)
    
    print(f"Win Margin: {total}")
    return total

if __name__ == "__main__":
    print("Part 1 Test: ", solve('test_data.txt'))
    print("Part 1: ", solve('data.txt'))

    print("Part 2 Test:", solve('test_data.txt', part2=True))
    print("Part 2:", solve('data.txt', part2=True))