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

def count_routes(lines):
    line_arrays = [list(line) for line in lines]
    # replace '0' with 0
    for i in range(len(line_arrays)):
        for j in range(len(line_arrays[i])):
            if line_arrays[i][j] == '.':
                line_arrays[i][j] = 0
    for i in range(1,len(line_arrays)):
        # for each line except the first one

        line = line_arrays[i]
        # replace . with 0
        for j in range(len(line)):
            above_value = line_arrays[i-1][j]
            above_is_number = isinstance(above_value, int)
            value = line[j]
            if above_value == 'S':
                    line[j] = 1
            elif above_is_number and value == '^':
                if j>0 and isinstance(line[j-1], int):
                    line[j-1] += above_value
                if j<len(line)-1 and isinstance(line[j+1], int):
                    line[j+1] += above_value
            elif above_is_number:
                line[j] += above_value
        line_with_spaces = ['  ' if x == 0 else str(x) + ' ' for x in line]
       # print(''.join([str(x)+' ' for x in line_with_spaces ]))

    sum_of_last_line = sum(line_arrays[-1])
    possible_routes = sum_of_last_line
    
    return possible_routes 

if __name__ == '__main__':
    test_routes = count_routes(test_lines)
    if test_routes!= 40:
        raise ValueError(f'Expected 40 routes, but got {test_routes}')

    with open('input.txt', 'r') as f:
        lines = f.readlines()
        print(f'Part 1: {count_routes(lines)}')