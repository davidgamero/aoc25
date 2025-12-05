input_file = 'input.txt'

def get_max_joltage(line:str) -> int:
    # get first largest integer from a line of text, and its index
    numbers = [int(s) for s in line if s.isdigit()]
    numbers_without_last = numbers[:-1]
    max_number = max(numbers_without_last)
    index_of_max = numbers_without_last.index(max_number)

    numbers_after_max = numbers[index_of_max + 1:]
    second_max = max(numbers_after_max) if numbers_after_max else None
    value = max_number*10 + second_max
    return value


assert(get_max_joltage("811111111111119"),89)

with open(input_file, 'r') as file:
    lines = file.readlines()

    total_value = 0
    for line in lines:
        line_value = get_max_joltage(line.strip())
        total_value += line_value
    print(f"Total Value: {total_value}")