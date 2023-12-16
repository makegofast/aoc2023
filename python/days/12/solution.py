import re

def read_file(filename):
    for line in open(filename).read().splitlines():
        f1, f2 = line.split()
        f2 = [int(c) for c in f2.split(',')]

        yield f1, f2
    
def check(b, rep):
    b = b.replace('.', ' ')
    return rep.match(b) != None

def fluff(f1, f2, dlen, matches, fpos=0, rep=None):
    if not rep:
        pattern = f1.replace('.', ' ').replace('?', '.') 
        rep = re.compile(pattern)

    for i in range(0, dlen+1):
        nf2 = f2.copy()
        nf2[fpos] = ('.'*i) + nf2[fpos]

        nf1 = '.'.join(nf2).ljust(len(f1), '.') 

        #print(f"dlen {dlen} fpos {fpos}")
        #print(" f1:", f1)
        match = check(nf1, rep)
        if match:
            matches[nf1] = True

        #print(f1, "nf1:", nf1, match)

        #if check(f1, nf1):
        #    matches[nf1] = True 

        if fpos+1 < len(nf2):
            fluff(f1, nf2, dlen-i, matches, fpos+1, rep)
        
    return matches 

def solve(filename, part2=False):
    data = read_file(filename)

    total = 0
    for f1, f2 in read_file(filename):
        print(f1, f2)

        nf2 = ['#'*n for n in f2]
        dlen = len(f1) - len('.'.join(nf2))
        #print(nf2, dlen)
        #print(f1, f2)

        matches = {}
        fluff(f1, nf2, dlen, matches)
        print(f1)
        print("matches", '\n'.join([str(m) for m in matches]))

        total += len(matches)

        #if part2:
        #    p2f1 = '?'.join([f1 for _ in range(0,5)])
        #    print('p2f1:', p2f1)
        #    calc_part2(p2f1, matches)
    
    return total

if __name__ == "__main__":
    #print("Part 1 Test: ", solve('test_data.txt'))
    #print("Part 1: ", solve('data.txt'))

    print("Part 2 Test:", solve('test_data.txt', True))
    #print("Part 2 Test (100):", solve('test_data.txt', 100))