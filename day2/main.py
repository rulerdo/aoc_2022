
def parse_data(filename):

    with open(filename) as d:
        data = d.read()

    return data


def evaluate_match(line):

    shape_value = {
        'X' : 1,
        'Y' : 2,
        'Z' : 3,
    }

    winners = ['A Y','B Z','C X']
    ties = ['A X','B Y','C Z']

    me = line[-1]

    if line in winners:
        result = shape_value.get(me) + 6

    elif line in ties:
        result = shape_value.get(me) + 3

    else:
        result = shape_value.get(me)
    
    return result



def evaluate_match_part2(line):

    shape_value = {
        'A' : 1,
        'B' : 2,
        'C' : 3,
    }

    if line[-1] == 'X':
        add = 0
        if line[0] == 'A':
            me = 'C'
        elif line[0] == 'B':
            me = 'A'
        else:
            me = 'B'

    elif line[-1] == 'Y':
        add = 3
        me = line[0]

    else:
        add = 6
        if line[0] == 'A':
            me = 'B'
        elif line[0] == 'B':
            me = 'C'
        else:
            me = 'A'

    result = add + shape_value.get(me)

    return result

def part1(data):

    datalist = data.splitlines()
    score = 0

    for line in datalist:
        result = evaluate_match(line)
        score += result

    return score


def part2(data):
    
    datalist = data.splitlines()
    score = 0

    for line in datalist:
        result = evaluate_match_part2(line)
        score += result

    return score


if __name__ == '__main__':

    data = parse_data('data.txt')
    result_p1 = part1(data)
    print(f'Answer Part1: {result_p1}') if result_p1 else ''
    result_p2 = part2(data)
    print(f'Answer Part2: {result_p2}') if result_p2 else ''
