with open("input", "r") as f:
    lines = f.readlines()

# current position
p = 50
zeros = 0
for line in lines:
    dir = line[0]
    digits = line[1:-1]

    # rotate
    sign = 1
    if dir == "L":
        sign = -1
    p += (sign * int(digits))
    p = p%100
    print(f'"{line[:-1]}" d={dir} d={digits} s={sign} p={p}')

    # check if rotation resulted in 0
    if p == 0:
        zeros += 1
print("zeros = " + str(zeros))

