def count_unique_ingredients(lines):
    fresh_ranges = []
    ingredients = []
    for line in lines:
        if line == '':
            continue
        if '-' in line:
            parts = line.split('-')
            fresh_ranges.append((int(parts[0]), int(parts[1])))
        else:
            ingredients.append(int(line))

    fresh_ingredient_set = set()
    for ingredient in ingredients:
        for fresh_range in fresh_ranges:
            if fresh_range[0] <= ingredient <= fresh_range[1]:
                fresh_ingredient_set.add(ingredient)
                break

    unique_nonoverlapping_ranges = []
    for fresh_range in fresh_ranges:
        overlapping_ranges = []
        for existing_range in unique_nonoverlapping_ranges:
            # Check for overlap
            if max(fresh_range[0], existing_range[0]) <= min(fresh_range[1], existing_range[1]):
                overlapping_ranges.append(existing_range)
        
        if overlapping_ranges:
            new_min = fresh_range[0]
            new_max = fresh_range[1]
            for existing_range in overlapping_ranges:
                unique_nonoverlapping_ranges.remove(existing_range)
                new_min = min(new_min, existing_range[0])
                new_max = max(new_max, existing_range[1])
            unique_nonoverlapping_ranges.append((new_min, new_max))
        else:
            unique_nonoverlapping_ranges.append(fresh_range)

    # total number of unqiue ingredients in unique nonoverlapping ranges
    total_unique_ingredients = 0
    for fresh_range in unique_nonoverlapping_ranges:
        total_unique_ingredients += fresh_range[1] - fresh_range[0] + 1
    return total_unique_ingredients

if __name__ == "__main__":
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
    test_unique_ingredients = count_unique_ingredients(testlines)
    print(f'test: {test_unique_ingredients}')  # Expected output: 10
    if test_unique_ingredients != 14:
        raise Exception('Test failed')

    with open('05/input.txt', 'r') as file:
        lines = [line.strip() for line in file.readlines()]
        
        unique_ingredients = count_unique_ingredients(lines)
        print(f'unique ingredients: {unique_ingredients}')