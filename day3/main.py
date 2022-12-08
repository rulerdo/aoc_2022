import string
import itertools

def parse_data(filename):

    with open(filename) as d:
        data = d.read()

    return data

def split_list(line):
    half = len(line)//2
    return line[:half], line[half:]


def find_dups(list1,list2):
    
    dup = set(list1) & set(list2)

    if dup:
        return list(dup)[0]
    else:
        return None
 
def find_dups_part2(group):

    dup = set(group[0]) & set(group[1]) & set(group[2])

    if dup:
        return list(dup)[0]
    else:
        return None

def create_alphabet_dict():

    all_letters = string.ascii_lowercase + string.ascii_uppercase

    i = 1
    item_values = {}

    for letter in all_letters:
        item_values[letter] = i
        i += 1

    return item_values


def grouper(n, rucksacks, fillvalue=None):

    args = [iter(rucksacks)] * n
    groups = itertools.zip_longest(*args, fillvalue=fillvalue)
    
    return list(groups)



def part1(data):

    rows = data.splitlines()
    rucksacks = [list(row) for row in rows]
    priorities = 0
    item_values = create_alphabet_dict()

    for line in rucksacks:
        list1 , list2 = split_list(line)
        dup = find_dups(list1,list2)
        if dup:
            priorities += item_values[dup]

    return priorities    


def part2(data):

    rows = data.splitlines()
    rucksacks = [list(row) for row in rows]
    priorities = 0
    item_values = create_alphabet_dict()
    groups = grouper(3,rucksacks)

    for group in groups:

        dup = find_dups_part2(group)
        if dup:
            priorities += item_values[dup]
        
    return priorities


if __name__ == '__main__':

    data = parse_data('data.txt')
    result_p1 = part1(data)
    print(f'Answer Part1: {result_p1}') if result_p1 else ''
    result_p2 = part2(data)
    print(f'Answer Part2: {result_p2}') if result_p2 else ''
