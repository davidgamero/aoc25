import math

with open("input", "r") as f:
    lines = f.readlines()

def crosses_zero(start_pos, end_pos, is_clockwise):
    """
    Check if rotation from start_pos to end_pos crosses position 0.
    Returns number of zero crossings.
    """
    if start_pos == end_pos:
        return 0
    
    if is_clockwise:
        # Clockwise: crossing 0 means going from high numbers to low numbers
        if start_pos < end_pos:
            # Wrapped around: e.g., 90 -> 10 (crossed 0/100)
            return 1
        else:
            # Normal movement: e.g., 30 -> 10 (no crossing)
            return 0
    else:
        # Counter-clockwise: crossing 0 means going from low numbers to high numbers
        if start_pos > end_pos:
            # Wrapped around: e.g., 10 -> 90 (crossed 0/100)
            return 1
        else:
            # Normal movement: e.g., 10 -> 30 (no crossing)
            return 0

# current position
p = 50
zeros = 0

for line in lines:
    old_p = p
    dir = line[0]
    digits = line[1:-1]
    
    ticks = int(digits)
    is_clockwise = (dir == "R")
    
    print(f'"{line[:-1]}" d={dir} ticks={digits} p{old_p}')
    
    # Count full rotations (each full rotation passes through 0 once)
    full_rots = ticks // 100
    if full_rots > 0:
        print(f'  adding {full_rots} for full rotations')
        zeros += full_rots
        print(f'  z = {zeros}')
    
    # Calculate the remaining partial rotation
    remaining_ticks = ticks % 100
    if remaining_ticks > 0:
        if is_clockwise:
            new_p = (old_p + remaining_ticks) % 100
        else:
            new_p = (old_p - remaining_ticks) % 100
        
        # Check if the partial rotation crosses zero
        zero_crossings = crosses_zero(old_p, new_p, is_clockwise)
        if zero_crossings > 0:
            print(f'  partial rotation crosses zero')
            zeros += zero_crossings
            print(f'  z = {zeros}')
        
        p = new_p
    else:
        # No remaining rotation after full rotations
        p = old_p
    
    print(f'  p {old_p}>{p}')

print("zeros = " + str(zeros))
