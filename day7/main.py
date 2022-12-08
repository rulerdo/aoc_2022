
def parse_data(filename):

    with open(filename) as d:
        data = d.read().splitlines()

    return data


def get_subdirectories(data,parent):

    subdir = []
    for i in range(len(data)):
        if  data[i]== f'$ cd {parent}':
            dir_starts_at = i
            print(dir_starts_at)
            break

    for i in range(dir_starts_at + 1,len(data)):
        if  '$ cd' in data[i]:
            dir_ends_at = i
            print(dir_ends_at)
            break

    for i in range(dir_starts_at,dir_ends_at):
        if data[i][:4] == 'dir ':
            subdir.append(data[i][-(len(data[i])-4):])

    return subdir


def get_size(filename):

    filelist = filename.split(' ')
    numlist = filelist[0].split('/')
    size = int(numlist[-1])

    return size

def part1(data):

    current_dir = []
    directories = ['/']
    files = []

    for line in data:

        if '$ cd ' in line and line != '$ cd ..':
            current_dir.append(line[-(len(line)-5):])
        
        elif line == '$ ls':
            pass

        elif 'dir ' in line:
            new_directory = '/'.join(current_dir) + '/' + line[-(len(line)-4):]
            directories.append(new_directory[1:])

        elif line == '$ cd ..':
            current_dir.pop(-1)

        else:
            new_file = '/'.join(current_dir) + '/' + line
            files.append(new_file[1:])

    directory_size_dict = {}

    for dir in directories:
        directory_size_dict[dir] = 0
        for file in files:
            if dir in file:
                size = get_size(file)
                directory_size_dict[dir] += size

    total = 0
    for value in directory_size_dict.values():
        if value <= 100_000:
            total += value

    return total,directory_size_dict


def part2(directory_size_dict):
    
    total_space = 70_000_000
    used_space = directory_size_dict['/']
    unused_space = total_space - used_space
    space_needed = 30_000_000 - unused_space
    space_found = 70_000_000

    for value in directory_size_dict.values():
        if value > space_needed and value < space_found:
            space_found = value

    return space_found

if __name__ == '__main__':

    data = parse_data('data.txt')
    result_p1,directory_size_dict = part1(data)
    print(f'Answer Part1: {result_p1}') if result_p1 else ''
    result_p2 = part2(directory_size_dict)
    print(f'Answer Part2: {result_p2}') if result_p2 else ''
