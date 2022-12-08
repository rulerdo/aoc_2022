
def parse_data(filename):

    with open(filename) as d:
        raw_data = d.read().splitlines()

    data = []
    
    for line in raw_data:
        two_pairs = line.split(',')
        pair1 = two_pairs[0].split('-')
        pair2 = two_pairs[1].split('-')
        new_line = [(int(pair1[0]),int(pair1[1])),(int(pair2[0]),int(pair2[1]))]
        data.append(new_line)

    return data


def part1(data):

    contained = 0

    for line in data:
        p1s = line[0][0]
        p1e = line[0][1]
        p2s = line[1][0]
        p2e = line[1][1]

        if (p1s >= p2s and p1e <= p2e) or (p2s >= p1s and p2e <= p1e):
            contained += 1

    return contained


def part2(data):

    contained = 0

    for line in data:
        add = False
        p1s = line[0][0]
        p1e = line[0][1]
        p2s = line[1][0]
        p2e = line[1][1]

        if p1s in range(p2s,p2e + 1):
            add = True

        elif p1e in range(p2s,p2e + 1):
            add = True

        elif p2s in range(p1s,p1e + 1):
            add = True

        elif p2e  in range(p1s,p1e + 1):
            add = True

        if add:
            contained += 1
        
    return contained


if __name__ == '__main__':

    data = parse_data('data.txt')
    result_p1 = part1(data)
    print(f'Answer Part1: {result_p1}') if result_p1 else ''
    result_p2 = part2(data)
    print(f'Answer Part2: {result_p2}') if result_p2 else ''
