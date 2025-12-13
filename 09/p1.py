import numpy as np

test_input = '''7,1
11,1
11,7
9,7
9,5
2,5
2,3
7,3'''
test_lines = [l.strip() for l in test_input.split("\n")]

def extract_points(lines):
    points = []
    for l in lines:
        stripped = l.strip()
        split = stripped.split(",")
        strings = [s.strip() for s in split]
        ints = [int(s) for s in strings]
        points.append(ints)
    return points

def max_area(points):
    max_p1 = [-1,-1]
    max_p2 = [-1,-1]
    max_area = -1
    for p1 in points:
        for p2 in points:
            delta0 = p1[0] - p2[0] +1 # includes border
            delta1 = p1[1] - p2[1] +1 # includes border
            area = np.abs(delta0 * delta1)
            if area > max_area:
                max_area = area
                max_p1 = p1
                max_p2 = p2
    return max_area, max_p1, max_p2

if __name__ == "__main__":
    test_points = extract_points(test_lines)
    test_max_area= max_area(test_points)
    print(test_max_area)

    with open('input.txt') as f:
        lines = f.readlines()

        points = extract_points(lines)
        max_area,p1,p2 = max_area(points)
        print("real: ",max_area, p1, p2)