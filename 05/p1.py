

test_input = '''
3-5
10-14
16-20
12-18

1
5
8
11
17
32
'''
testlines = test_input.strip().split('\n')

with open('05/input.txt', 'r') as file:
    lines = [line.strip() for line in file.readlines()]
    
    # split on empty line
    fresh_range_lines = []
    ingredient_lines = []
    for line in lines:
        if line == '':
            continue
        if '-' in line:
            fresh_range_lines.append(line)
            current_group = []
        else:
            ingredient_lines.append(line)
    
    fresh_ranges = []
    for line in fresh_range_lines:
        parts = line.split('-')
        fresh_ranges.append((int(parts[0]), int(parts[1])))
    ingredients = []
    for line in ingredient_lines:
        ingredients.append(int(line))

    fresh_ingrendient_set = set()
    for ingredient in ingredients:
        for fresh_range in fresh_ranges:
            if fresh_range[0] <= ingredient <= fresh_range[1]:
                fresh_ingrendient_set.add(ingredient)
                break
    
    
    print(fresh_ranges)
    print(ingredients)

    fresh_ingredient_count = len(fresh_ingrendient_set)
    print(f'fresh_ingredient_count: {fresh_ingredient_count}')