
input_file = 'input.txt'

def is_valid_id(id):
    length = len(id)
    divisible_lengths = [l for l in range(1, length) if length % l == 0]
    for l in divisible_lengths:
        # split into chunks of length l
        chunks = [id[i:i+l] for i in range(0, length, l)]
        all_chunks_equal = all(chunk == chunks[0] for chunk in chunks)
        if all_chunks_equal:
            return False
    return True

assert is_valid_id('12') == True
assert is_valid_id('38593859') == False
assert is_valid_id('2121212121') == False

def invalid_ids_in_range(x,y):
    invalid_ids_in_range = []
    for i in range(x, y + 1):
        id_str = str(i)
        if not is_valid_id(id_str):
            invalid_ids_in_range.append(i)
    return invalid_ids_in_range

assert invalid_ids_in_range(11, 22) == [11,22]

with open(input_file, 'r') as file:
    lines = file.readlines()

    line0 = lines[0].strip()

    ranges_string = line0.split(',')

    invalid_ids_in_ranges = []
    for r in ranges_string:
        x, y = map(int, r.split('-'))
        invalid_ids = invalid_ids_in_range(x, y)
        invalid_ids_in_ranges.extend(invalid_ids)
    
    sum_of_invalid_ids = sum(invalid_ids_in_ranges)
    print(f'Sum of invalid IDs: {sum_of_invalid_ids}')
