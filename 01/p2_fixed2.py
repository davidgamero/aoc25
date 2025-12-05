import math

with open("input", "r") as f:
    lines = f.readlines()

# current position
p = 50
zeros = 0

for line in lines:
    old_p = p
    dir = line[0]
    digits = line[1:-1]
    
    # rotate
    ticks = int(digits)
    sign = 1 if dir == "R" else -1
    
    print(f'"{line[:-1]}" d={dir} d={digits} s={sign} p{old_p}')
    
    # Count how many times we pass through 0 during this rotation
    # For each tick in the rotation, check if we land on 0
    clicks_through_zero = 0
    
    for i in range(1, ticks + 1):
        current_pos = (old_p + sign * i) % 100
        if current_pos == 0:
            clicks_through_zero += 1
    
    if clicks_through_zero > 0:
        print(f'  adding {clicks_through_zero} clicks through zero')
        zeros += clicks_through_zero
        print(f'  z = {zeros}')
    
    # Update position
    p = (old_p + sign * ticks) % 100
    print(f'  p {old_p}>{p}')

print("zeros = " + str(zeros))
