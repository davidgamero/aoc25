def is_valid_location(x, y, grid):
    return 0 <= y < len(grid) and 0 <= x < len(grid[0])


def get_neighbor_values(x,y,grid):
    values = []
    for dy in [-1,0,1]:
        for dx in [-1,0,1]:
            if dx == 0 and dy == 0:
                continue # Skip the center cell
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(grid[0]) and 0 <= ny < len(grid):
                values.append(grid[ny][nx])
    return values

ROLL_CHAR = '@'
def count_accessible_rolls(grid):
    accessible_roll_count = 0
    accessible_roll_locations = []
    neighbor_roll_count_grid = [[0] * len(grid[0]) for _ in range(len(grid))]
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            neighbor_values = get_neighbor_values(x, y, grid)
            neighbor_roll = [char for char in neighbor_values if char == ROLL_CHAR]
            neighbor_roll_count = len(neighbor_roll)
            neighbor_roll_count_grid[y][x] = neighbor_roll_count
            if grid[y][x] != ROLL_CHAR:
                continue
            if neighbor_roll_count < 4:
                accessible_roll_count += 1
                accessible_roll_locations.append((x, y))
    return accessible_roll_count, accessible_roll_locations, neighbor_roll_count_grid

test_grid_string =  '''
..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.
'''
test_grid_array = [list(line.strip()) for line in test_grid_string.strip().split('\n') if line.strip()]
test_count, test_locations, test_neighbor_roll_count_grid = count_accessible_rolls(test_grid_array) 
# replace accessible locations with x in print grid
print("Neighbor roll count grid:")
for row in test_neighbor_roll_count_grid:
    print(''.join(str(cell) if cell != 0 else '.' for cell in row))
print()

print("Accessible rolls and their locations:")
for x, y in test_locations:
    test_grid_array[y][x] = 'x'
for row in test_grid_array:
    print(''.join(row)) 
print()
if test_count != 13:
    print("Test failed: Expected 13 accessible rolls, but got", test_count)
    assert False


with open('input.txt', 'r') as file:
    lines = [line.strip() for line in file.readlines() if line.strip()]
    rows = len(lines)
    cols = len(lines[0].strip())

    accessible_roll_count = count_accessible_rolls(lines)
    print("Number of accessible rolls:", accessible_roll_count)