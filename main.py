import random

print("Starting to code Galactic Finance Game")


def func_itr():
    while True:
        yield round(random.random(), 2)


rnd_num = func_itr()
print(rnd_num.__next__())
print(rnd_num.__next__())
print(rnd_num.__next__())

