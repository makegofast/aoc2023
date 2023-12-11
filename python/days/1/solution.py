def read_file(filename):
    return open(filename).read().splitlines()

def convert_number_words_to_numbers(line):
    word_map = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    max_buffer= max([len(w) for w in word_map])

    start = 0
    end = len(line)
    while start < len(line):
        chunk = line[start:start+max_buffer]
        #print(chunk)
        for num, word in enumerate(word_map):
            if chunk.startswith(word):
                print(f" Before: {line}")
                line = line[0:start] + str(num) + line[start+len(word):]
                #print(f"New line: {line}")
                print(f"Updated: {line}")

        start += 1
    
    return line
    
def solve(filename, part2=False):
    data = read_file(filename)

    calibration_values = []
    total = 0

    for line in data:
        print("Line: ", line)

        if part2:
            line = convert_number_words_to_numbers(line)
            print("Conv: ", line)

        numbers = [c for c in line.strip() if c.isnumeric()]
        first, last = numbers[0], numbers[-1] 
        print(f"Numbers: {numbers}, First: {first}, Last: {last}")

        cal_val = int(f"{first}{last}")
        calibration_values.append(cal_val)
        
        print(f"{total} + {cal_val} = {total+cal_val}")
        print()

        total += cal_val

    print(calibration_values)
    print(len(calibration_values))

    print(f"Calibration Value: {total}")
    print(f"Check: {sum(calibration_values)}")

    return total

if __name__ == "__main__":
    print("Part 1 Test: ", solve('test_data.txt'))
    print("Part 1: ", solve('data.txt'))

    print("Part 2 Test:", solve('test_data_2.txt', part2=True))
    print("Part 2 Bancroft:", solve('bancroft.txt', part2=True))
    #print("Part 2:", solve('data.txt', part2=True)) #broken