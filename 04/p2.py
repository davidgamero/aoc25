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
def remove_accessible_rolls(grid):
    removed_roll_count = 0
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
            is_accessible= neighbor_roll_count < 4
            if is_accessible:
                removed_roll_count += 1
                accessible_roll_locations.append((x, y))
                # replace char x in string y
                grid[y][x] = 'x'
    return removed_roll_count, accessible_roll_locations, neighbor_roll_count_grid




with open('input.txt', 'r') as file:
    lines = [line.strip() for line in file.readlines() if line.strip()]
    rows = len(lines)
    cols = len(lines[0].strip())

    # break lines into list of 1 char strings
    lines = [[char for char in line] for line in lines]

    total_removed = 0
    while True:
        removed_count,_,_ = remove_accessible_rolls(lines)
        if removed_count == 0:
            break
        total_removed += removed_count
    print("Number of accessible rolls removed:", total_removed)