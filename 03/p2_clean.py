def get_max_joltage(line:str, joltage_digits_count:int=12) -> int:
    numbers = [int(s) for s in line if s.isdigit()]
    i_max_used, value = -1, 0

    for i in range(joltage_digits_count, 0, -1):
        # don't consider last i digits or we won't be able get get enough
        end_numbers_to_remove = i - 1
        numbers_without_last = numbers[:-end_numbers_to_remove] if end_numbers_to_remove > 0 else numbers

        numbers_usable = numbers_without_last[i_max_used + 1:]
        max_usable = max(numbers_usable)
        i_max_used = numbers_usable.index(max_usable) + i_max_used + 1

        value = value * 10 + max_usable
    return value

assert(get_max_joltage("891111111111111",2)==91)
assert(get_max_joltage("891111111111711",3)==971)
assert(get_max_joltage("811111111111119",2)==89)
assert(get_max_joltage("234234234234278")==434234234278)
assert(get_max_joltage("818181911112111")==888911112111)

with open('input.txt', 'r') as file:
    total_value = 0
    for line in file.readlines():
        total_value += get_max_joltage(line.strip())
    print(f"Total Value: {total_value}")