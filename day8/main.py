
def parse_data(filename):

    with open(filename) as d:
        data = d.read().splitlines()
        
    data_matrix = []

    for row in data:
        new_row = [int(i) for i in row]
        data_matrix.append(new_row)

    return data_matrix


def part1(data):

    nCols = len(data[0])
    nRows = len(data)
    visible_trees = (nCols * 2) + (nRows * 2) - 4

    for x in range(1, nRows - 1):
        for y in range(1, nCols - 1):
            tree = data[x][y]
            upTrees = [data[i][y] for i in range(0,x)]
            downTrees = [data[i][y] for i in range(x+1,nRows)]
            leftTrees = [data[x][i] for i in range(0,y)]
            rightTrees = [data[x][i] for i in range(y+1,nCols)]
            
            check_trees = [
                all(t < tree for t in upTrees),
                all(t < tree for t in downTrees),
                all(t < tree for t in leftTrees),
                all(t < tree for t in rightTrees),
            ]

            if any(check_trees):
                visible_trees += 1

    return visible_trees


def directional_score(tree,treelist):

    if all(t < tree for t in treelist):
        dScore = len(treelist)

    else:

        dScore = 1
        for t in treelist:
            if tree > t:
                dScore += 1
            else:
                break
    
    return dScore


def part2(data):

    nCols = len(data[0])
    nRows = len(data)
    score = 0

    for x in range(1, nRows - 1):
        for y in range(1, nCols - 1):
            tree = data[x][y]
            upTrees = [data[i][y] for i in reversed(range(0,x))]
            downTrees = [data[i][y] for i in range(x+1,nRows)]
            leftTrees = [data[x][i] for i in reversed(range(0,y))]
            rightTrees = [data[x][i] for i in range(y+1,nCols)]

            upScore = directional_score(tree,upTrees)
            downScore = directional_score(tree,downTrees)
            leftScore = directional_score(tree,leftTrees)
            rightScore = directional_score(tree,rightTrees)
            testScore = upScore * downScore * leftScore * rightScore

            if score < testScore:
                score = testScore
               
    return score
            


if __name__ == '__main__':

    data = parse_data('data.txt')
    result_p1 = part1(data)
    print(f'Answer Part1: {result_p1}') if result_p1 else ''
    result_p2 = part2(data)
    print(f'Answer Part2: {result_p2}') if result_p2 else ''