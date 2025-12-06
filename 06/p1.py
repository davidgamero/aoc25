
def separate_problems(lines: list[list[str]]) -> list[tuple[str, list[list[str]]]]: 
    problems = []
    new_problem_op = ''
    new_problem_cols = []
    for col in range(len(lines[0])):
        is_first_new_prob_col = len(new_problem_cols) == 0
        col_values = [lines[row][col] for row in range(len(lines))] 
        if is_first_new_prob_col:
            new_problem_op = col_values[-1]
        col_is_empty = all([x.strip() == '' for x in col_values])
        is_last_col = col == len(lines[0]) - 1
        if is_last_col:
            new_problem_cols.append(col_values)
        if col_is_empty or is_last_col:
            problems.append((new_problem_op, new_problem_cols))
            new_problem_op = ''
            new_problem_cols = []
            continue
        new_problem_cols.append(col_values)
    return problems

def parse_problems(problems: list[tuple[str, list[list[str]]]]) -> list[tuple[str, list[int]]]:
    parsed_problems = []
    for op,cols in problems:
        parsed_row_vals = []
        for i in range(len(cols[0])-1):
            row_val = ''
            for col in cols:
                row_val += col[i].strip()
            parsed_row_vals.append(int(row_val))
        parsed_problems.append((op, parsed_row_vals))
    return parsed_problems

OPFUNCS = {
    '+': lambda x,y: x+y,
    '-': lambda x,y: x-y,
    '*': lambda x,y: x*y,
    '/': lambda x,y: x/y,
}

def get_problems_sum(problems: list[tuple[str, list[int]]]) -> int:
    total_sum = 0
    for op,vals in problems:
        op_func = OPFUNCS[op]
        result = vals[0]
        for val in vals[1:]:
            result = op_func(result, val)
        total_sum += result
    return total_sum

test_text = '''
123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  
'''

if __name__ == "__main__":
    test_lines = [list(line) for line in test_text.split('\n') if line != '']
    test_prob_cols = separate_problems(test_lines)
    test_probs = parse_problems(test_prob_cols)
    test_sum = get_problems_sum(test_probs)
    if test_sum != 4277556:
        print('Test failed')
        raise Exception(f'test_sum: {test_sum}')
    
    with open('input.txt', 'r') as f:
        lines = [list(line) for line in f.read().split('\n') if line != '']
        prob_cols = separate_problems(lines)
        probs = parse_problems(prob_cols)
        sum = get_problems_sum(probs)
        print(f'sum: {sum}')
