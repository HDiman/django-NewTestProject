# import random
#
# print("Starting to code Galactic Finance Game")
#
#
# def func_itr():
#     while True:
#         yield int(random.random() * 100)
#
#
# rnd_num = func_itr()
# print(rnd_num.__next__())
# print(rnd_num.__next__())
# print(rnd_num.__next__())
#
#
# lst = [1, 2, 3, 4, 5]
# new_list = list(map(lambda x: x*2, lst))
# print(new_list)
#
#
#
# def make_important(fn):
#     def wrapped():
#         return "!" + fn() + "!"
#     return wrapped
#
# @make_important
# def hello():
#     return 'hello habr'
#
# print(hello())

# lst = ["first", "second", "third"]
# lst2 = []
# for index, value in enumerate(lst):
#     print(index, value)
#     lst2.append(value)
#
# print(list(reversed(lst2)))

lst = [True, True, True]
if any(lst):
    print("Some is True")
if all(lst):
    print("All is True")
