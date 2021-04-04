import numpy as np
import random


def max_contact(person_count: int) -> int:
    if person_count == 2:
        return 1
    else:
        return person_count - 1 + max_contact(person_count - 1)


def min_contact(person_count: int) -> int:
    return person_count


def gen_data_full_random(person_count: int, contact_count: int):
    matrix = np.zeros((person_count, person_count))
    while contact_count > 0:
        i = random.randint(0, person_count - 1)
        j = random.randint(0, person_count - 1)
        if matrix[i][j] == 0 and matrix[j][i] == 0 and i != j:
            contact_count -= 1
            matrix[i][j] = matrix[j][i] = 1

    return matrix


def gen_data_garanted_pass(person_count: int, contact_count: int):
    matrix = np.zeros((person_count, person_count))
    for i in range(0, person_count):
        while np.sum(matrix[i]) != 2:
            min_j = i + 1
            for j in range(0, person_count):
                if j == i:
                    continue
                if np.sum(matrix[j]) < np.sum(matrix[min_j]):
                    min_j = j
            matrix[i][min_j] = matrix[min_j][i] = 1
            contact_count -= 1

    while contact_count > 0:
        i = random.randint(0, person_count - 1)
        j = random.randint(0, person_count - 1)
        if matrix[i][j] == 0 and matrix[j][i] == 0 and i != j:
            contact_count -= 1
            matrix[i][j] = matrix[j][i] = 1

    return matrix
