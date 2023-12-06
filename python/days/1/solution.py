def part1(filename):
    data = open(filename).readlines()

    calibration_values = []

    for line in data:
        print(line.strip())
        numbers = [c for c in line.strip() if c.isnumeric()]
        calibration_values.append(int(''.join([numbers[0], numbers[-1]])))
    
    print(calibration_values)
    print(sum(calibration_values))

if __name__ == "__main__":
    part1('test_data.txt')
    part1('data.txt')