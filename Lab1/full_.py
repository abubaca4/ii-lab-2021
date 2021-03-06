import numpy as np
num_0 = 0


def find_path(start_point: int, matrix: np.array):
    person_count = matrix[start_point].size
    deep = np.zeros(1)
    return (find_path_r(start_point, start_point, np.zeros(person_count), matrix, [], deep), deep[0])


def find_path_r(current: int, start_point: int, is_visited: np.array, matrix: np.array, way: list, deep: np.array):
    deep[0] += 1
    is_visited[current] = 1
    way.append(current)
    if np.sum(is_visited) == is_visited.size and matrix[current][start_point]:
        way.append(start_point)
        return way
    for i in range(0, matrix[current].size):
        if not is_visited[i] and matrix[current][i]:
            result = find_path_r(
                i, start_point, is_visited.copy(), matrix, way.copy(), deep)
            if result != False:
                return result
    return False
