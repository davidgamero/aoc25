input_file = 'input.txt'


def get_max_joltage(line:str, joltage_digits_count:int=12) -> int:
    numbers = [int(s) for s in line if s.isdigit()]
    digits_to_use = []
    i_max_used = -1

    for i in range(joltage_digits_count, 0, -1):
        # don't consider last i digits or we won't be able get get enough
        end_numbers_to_remove = i - 1

        numbers_without_last = numbers[:-end_numbers_to_remove] if end_numbers_to_remove > 0 else numbers

        numbers_after_used_before_last = numbers_without_last[i_max_used + 1:]
        max_usable = max(numbers_after_used_before_last)
        i_usable = numbers_after_used_before_last.index(max_usable) + i_max_used + 1
        i_max_used = i_usable

        digits_to_use.append(max_usable)

    # compute value as int of concatenated digits
    value = 0
    for d in digits_to_use:
        value = value * 10 + d
    return value


assert(get_max_joltage("891111111111111",2)==91)
assert(get_max_joltage("891111111111711",3)==971)
assert(get_max_joltage("811111111111119",2)==89)
assert(get_max_joltage("234234234234278")==434234234278)
assert(get_max_joltage("818181911112111")==888911112111)

with open(input_file, 'r') as file:
    lines = file.readlines()

    total_value = 0
    for line in lines:
        line_value = get_max_joltage(line.strip())
        total_value += line_value
    print(f"Total Value: {total_value}")