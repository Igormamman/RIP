import random


def gen_random(num_count, begin, end):
    # Необходимо реализовать генератор
    while num_count>0:
        num_count-=1
        yield random.randint(begin,end+1)

