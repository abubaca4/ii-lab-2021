import random
from generator import gen_data_garanted_pass, max_contact, min_contact
from full_ import find_path as brute_force
from opt import find_path as optimized
from draw import draw_graph


def test_one_time(person_count: int):
    con_count = random.randint(min_contact(person_count),
                               max_contact(person_count))
    data = gen_data_garanted_pass(person_count, con_count)
    result_1 = brute_force(0, data)
    print(result_1[0])
    print(result_1[1])
    if result_1[0]:
        draw_graph(data, result_1[0])
    result_2 = optimized(0, data)
    print(result_2[0])
    print(result_2[1])
    if result_2[0]:
        draw_graph(data, result_2[0])


def get_stat(person_count: int, try_count: int):
    res_1 = 0
    res_2 = 0

    for _ in range(0, try_count):
        con_count = random.randint(min_contact(person_count),
                                   max_contact(person_count))
        data = gen_data_garanted_pass(person_count, con_count)
        result_1 = brute_force(0, data)
        res_1 += result_1[1] / try_count
        result_2 = optimized(0, data)
        res_2 += result_2[1] / try_count

    print(person_count/res_1)
    print(person_count/res_2)


get_stat(13, 1000)
