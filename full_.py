import numpy as np


def find_path(start_point: int, matrix: np.array):
    person_count = matrix[start_point].size
    return find_path_r(start_point, start_point, np.zeros(person_count), matrix, [])


def find_path_r(current: int, start_point: int, is_visited: np.array, matrix: np.array, way: list):
    is_visited[current] = 1
    way.append(current)
    for i in range(0, matrix[current].size):
        if not is_visited[i] and matrix[current][i]:
            result = find_path_r(i, start_point, is_visited, matrix, way)
            if result != False:
                return result
    if np.sum(is_visited) == is_visited.size and matrix[current][start_point]:
        return way
    return False
