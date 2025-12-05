import math
from typing import Literal
RIGHT = 1
LEFT = -1

with open("input", "r") as f:
    lines = f.readlines()

def turn(dir_sign: Literal[-1, 1], ticks: int, p: int) -> tuple[int, int]: 
    ''' Returns new position and number of zeros passed through '''
    # count full rotations, which by definition add a zero
    zeros_passed = 0
    full_rots = math.floor(ticks/100)
    zeros_passed += full_rots

    remaining_ticks = ticks % 100
    # if no remaining ticks, return current position and full rotations counted
    if remaining_ticks == 0:
        return p, zeros_passed
    
    p_final_raw = p + dir_sign * remaining_ticks
    p_final = p_final_raw % 100
    if (p_final == 0 and p != 0) or (dir_sign == 1 and p_final_raw >= 100) or (dir_sign == -1 and p_final_raw < 0):
        zeros_passed += 1
    return p_final, zeros_passed

def turn_slow(dir_sign: Literal[-1, 1], ticks: int, p: int) -> tuple[int, int]: 
    ''' Returns new position and number of zeros passed through '''
    new_p = p
    zeros_passed_or_landed_on = 0
    for _ in range(ticks):
        new_p = (new_p + dir_sign) % 100
        if new_p == 0:
            zeros_passed_or_landed_on += 1

    return new_p, zeros_passed_or_landed_on
    

#tests
cases = [
    (LEFT, 150, 50),
    (LEFT, 150, 0),
    (LEFT, 52, 52),
    (RIGHT, 150, 50),
    (RIGHT, 150, 0),
    (LEFT, 100, 0),
    (LEFT, 200, 0),
    (RIGHT, 1, 99),
    (RIGHT, 301, 99),
]
# # compare slow and fast versions
# for dir_sign, ticks, start_p in cases:
#     p_slow, zeros_passed_slow = turn_slow(dir_sign, ticks, start_p)
#     p_fast, zeros_passed_fast = turn(dir_sign, ticks, start_p)
#     if p_fast != p_slow or zeros_passed_fast != zeros_passed_slow:
#         print(f"Mismatch for case ({dir_sign}, {ticks}, {start_p}): Fast p {p_fast}, zeros {zeros_passed_fast} != Slow p {p_slow}, zeros {zeros_passed_slow}")
#         assert False, "Mismatch between fast and slow implementations"

# current position
p = 50
zeros = 0
for line in lines:
    old_p = p
    dir = line[0]
    digits = line[1:-1]

    # rotate
    sign = 1
    ticks = int(digits)
    if dir == "L":
        sign = -1
    print(f'"{line[:-1]}" d={dir} d={digits} s={sign} p{old_p}')


    p, zeros_passed = turn(sign, ticks, old_p)
    
    # comapre with slow version
    p_slow, zeros_passed_slow = turn_slow(sign, ticks, old_p)

    zeros += zeros_passed_slow
    print(f'  p {old_p}>{p}')

print("zeros = " + str(zeros))

