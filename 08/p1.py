import numpy as np
import pandas as pd

test_text = '''162,817,812
57,618,57
906,360,560
592,479,940
352,342,300
466,668,158
542,29,236
431,825,988
739,650,466
52,470,668
216,146,977
819,987,18
117,168,530
805,96,715
346,949,466
970,615,88
941,993,340
862,61,35
984,92,344
425,690,689'''
test_lines = test_text.strip().split('\n')

def get_distances(lines) -> np.ndarray:
    # omit empty lines
    lines = [line for line in lines if line.strip()]
    # convert lines to numpy array of integers
    points = np.array([list(map(int, line.split(','))) for line in lines])
    
    # copy points n times times to create a 3D array with each point
    points_on_col = points[np.newaxis, :, :]
    points_on_row = points[:, np.newaxis, :]
    # subtract the original points from each row to get delta vectors
    vector_differences = points_on_row - points_on_col

    
    # Calculate distance for each pair with vector norm
    distances = np.linalg.norm(vector_differences, axis=2)
    return distances, points_on_row 


def get_n_closest_points_indices(distances: np.ndarray, points_expanded, n):
    closest_indices = np.argsort(distances, axis=1)[:, 1:n+1]  # Exclude the point itself (distance 0)
    # calculate i,j indices of closest points
    i_indices = np.arange(distances.shape[0])[:, np.newaxis]
    return closest_indices

def get_n_circuit_product(lines, n):
    distances, points_expanded = get_distances(lines)
    closest_points_indices = get_n_closest_points_indices(distances, points_expanded, n)

    # each circuit is a set of indices of points, indices are from lines/points_expanded
    circuits_sets: list[set[int]] = []
    for indices in closest_points_indices:
        new_circuit_set = set(indices)
        # merge any existing circuit that intersects with the new circuit
        for existing_circuit in circuits_sets:
            if existing_circuit.intersection(new_circuit_set):
                new_circuit_set.update(existing_circuit)
                circuits_sets.remove(existing_circuit)
        # add the new merged circuit to the list
        circuits_sets.append(new_circuit_set)
    
    circuit_set_lengths = [len(circuit_set) for circuit_set in circuits_sets]
    circuit_set_lengths_product = np.prod(circuit_set_lengths)
    return circuit_set_lengths_product 

#test_distances = get_distances(test_lines)
test_circuit_product = get_n_circuit_product(test_lines, 3)
if test_circuit_product != 40:
    raise ValueError("Test failed: Expected product of circuit lengths is 40, but got", test_circuit_product)


if __name__ == '__main__':
    with open('input.txt', 'r') as file:
        input_lines = file.readlines()
    
        distances, points_expanded = get_distances(input_lines)
        closest_1k_points = get_n_circuit_product(input_lines, 1000)
        print("Closest 1000 points:")
        print(closest_1k_points)

        print("done")
    