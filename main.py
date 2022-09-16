import random

# print("Starting to code Galactic Finance Game")


def func_itr():
    while True:
        yield int(random.random() * 100)


rnd_num = func_itr()
# print(rnd_num.__next__())
# print(rnd_num.__next__())
# print(rnd_num.__next__())


lst = [1, 2, 3, 4, 5]
new_list = list(map(lambda x: x*2, lst))
print(new_list)
