test_input = '''.......S.......
...............
.......^.......
...............
......^.^......
...............
.....^.^.^.....
...............
....^.^...^....
...............
...^.^...^.^...
...............
..^...^.....^..
...............
.^.^.^.^.^...^.
...............'''
test_lines = test_input.split('\n')

def count_splits(lines):
    line_arrays = [list(line) for line in lines]
    split_count = 0
    for i in range(1,len(line_arrays)):
        # for each line except the first one

        line = line_arrays[i]
        for j in range(len(line)):
            above_value = line_arrays[i-1][j]
            value = line[j]
            if above_value == 'S':
                    line[j] = '|'
            elif above_value == '|' and value == '^':
                split_count += 1
                if j>0:
                    line[j-1] = '|'
                if j<len(line)-1:
                    line[j+1] = '|'
            elif above_value == '|' and value == '.':
                line[j] = '|'

    return split_count 

if __name__ == '__main__':
    test_splits = count_splits(test_lines)
    if test_splits != 21:
        raise ValueError(f'Expected 21 splits, but got {test_splits}')

    with open('input.txt', 'r') as f:
        lines = f.readlines()
        print(f'Part 1: {count_splits(lines)}')