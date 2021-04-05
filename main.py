import random
from generator import gen_data_garanted_pass, max_contact, min_contact
from full_ import find_path as brute_force
from opt import find_path as optimized

person_count = 10
con_count = random.randint(min_contact(person_count),
                           max_contact(person_count))
data = gen_data_garanted_pass(person_count, con_count)
result_1 = brute_force(0, data)
print(result_1)
result_2 = optimized(0, data)
print(result_2)
