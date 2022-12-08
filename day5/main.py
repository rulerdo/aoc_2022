def load_cranes(cranes_file):

    with open(cranes_file) as f:
        raw_cranes = f.read().splitlines()
    
    cranes = []
    for line in raw_cranes:
        for c in ['[',']',' ']:
            line = line.replace(c,'')
        row = list(line)
        cranes.append(row)

    rows = len(cranes)
    columns = len(cranes[0])

    for x in range(rows):
        for y in range(columns):
            if cranes[x][y] == '-':
                cranes[x][y] = ''

    return cranes


def load_stacks(cranes_file):

    cranes = load_cranes(cranes_file)
    stacks = {}

    for i in range(9):
        stacks[i+1] = [line[i] for line in cranes]
        stacks[i+1] = [e for e in stacks[i+1] if e.strip()]
        stacks[i+1].reverse()

    return stacks

def load_steps(steps_file):
    
    with open(steps_file) as f:
        raw_steps = f.read().splitlines()

    steps = [[int(line[0]),int(line[1]),int(line[2])] for line in [line.split(' ') for line in raw_steps]]

    return steps


def part1():

    stacks = load_stacks('cranes.txt')
    # _ = [print(k,' : ',v) for k,v in stacks.items()] # Print stacks
    steps = load_steps('steps.txt')
    # _ = [print(step) for step in steps] # Print steps
    for step in steps:

        n = step[0]
        source = step[1]
        destination = step[2]

        move = stacks[source][-n:]
        move.reverse()
        stacks[destination] += move
        del stacks[source][len(stacks[source]) -n:]

    top_stacks = []
    for i in range(9):
        top_stacks.append(stacks[i+1][-1])

    return ''.join(top_stacks)


def part2():
    stacks = load_stacks('cranes.txt')
    # _ = [print(k,' : ',v) for k,v in stacks.items()] # Print stacks
    steps = load_steps('steps.txt')
    # _ = [print(step) for step in steps] # Print steps
    for step in steps:

        n = step[0]
        source = step[1]
        destination = step[2]

        move = stacks[source][-n:]
        stacks[destination] += move
        del stacks[source][len(stacks[source]) -n:]

    top_stacks = []
    for i in range(9):
        top_stacks.append(stacks[i+1][-1])

    return ''.join(top_stacks)


if __name__ == '__main__':

    result_p1 = part1()
    print(f'Answer Part1: {result_p1}') if result_p1 else ''
    result_p2 = part2()
    print(f'Answer Part2: {result_p2}') if result_p2 else ''