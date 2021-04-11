import numpy as np


def find_path(start_point: int, matrix: np.array):
    person_count = matrix[start_point].size
    person_priority = sorted(range(0, person_count),
                             key=lambda people: np.sum(matrix[people]))
    deep = np.zeros(1)
    return (find_path_r(start_point, start_point, np.zeros(person_count), matrix, [], person_priority, deep), deep[0])


def find_path_r(current: int, start_point: int, is_visited: np.array, matrix: np.array, way: list, priority: list, deep: np.array):
    deep[0] += 1
    is_visited[current] = 1
    way.append(current)
    if np.sum(is_visited) == is_visited.size and matrix[current][start_point]:
        way.append(start_point)
        return way
    for i in priority:
        if not is_visited[i] and matrix[current][i]:
            result = find_path_r(
                i, start_point, is_visited.copy(), matrix, way.copy(), priority, deep)
            if result != False:
                return result
    return False
