
def parse_data(filename):

    with open(filename) as d:
        data = d.read()

    return list(data)


def process_signal(data,bucket_size):

    for i in range(len(data) - (bucket_size-1)):
        bucket = [data[x] for x in range(i,i + bucket_size)]
        if len(set(bucket)) == len(bucket):
            return i + bucket_size


def part1(data):
    return process_signal(data,4)


def part2(data):
    return process_signal(data,14)


if __name__ == '__main__':

    data = parse_data('data.txt')
    result_p1 = part1(data)
    print(f'Answer Part1: {result_p1}') if result_p1 else ''
    result_p2 = part2(data)
    print(f'Answer Part2: {result_p2}') if result_p2 else ''
