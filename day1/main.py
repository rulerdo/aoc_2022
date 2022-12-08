
def parse_data(filename):

    with open(filename) as d:
        data = d.read()

    return data


def part1(data):

    datalist = data.splitlines()
    elf_dict = {}
    elfnumber = 1
    count = 0

    for i in datalist:
        
        if i != '':
            count += int(i)
        else:
            elf_dict[f'elf{elfnumber}'] = count
            elfnumber += 1
            count = 0

    result_p1 = max(list(elf_dict.values()))

    return result_p1,elf_dict


def part2(elf_dict):

    values = list(elf_dict.values())
    svalues = sorted(values,reverse=True)
    result_p2 = svalues[0] + svalues[1] + svalues[2]

    return result_p2


if __name__ == '__main__':

    data = parse_data('data.txt')
    result_p1,elf_dict = part1(data)
    print(f'Answer Part1: {result_p1}') if result_p1 else ''
    result_p2 = part2(elf_dict)
    print(f'Answer Part2: {result_p2}') if result_p2 else ''
