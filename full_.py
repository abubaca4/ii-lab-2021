from generator import gen_data_garanted_pass, max_contact, min_contact
import numpy as np
import random


def find_path(current: int, start_point: int, is_visited: np.array, matrix: np.array, way: list):
    is_visited[current] = 1
    way.append(current)
    for i in range(0, matrix[current].size):
        if not is_visited[i] and matrix[current][i]:
            result = find_path(i, start_point, is_visited, matrix, way)
            if result != False:
                return result
    if np.sum(is_visited) == is_visited.size and matrix[current][start_point]:
        return way
    return False

person_count = 10
con_count = random.randint(min_contact(person_count),
                           max_contact(person_count))
data = gen_data_garanted_pass(person_count, con_count)
print(find_path(0, 0, np.zeros(person_count), data, []))
