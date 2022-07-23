days = ("sunday", "monday", "tuesday", "wednesday", "thursday")


def result(a, b):
    return a + b


# function with normal variables
print(result(100, 200))

# A tuple is created
c = (100, 300)

# Tuple is passed
# function unpacked them


# *b grammar only running on Python3
print(result(*c))

a, b, *c = (1, 2, 3, 4, 5, 6)  # tuple
print(a, b, c)  # 1, 2, [3, 4, 5, 6]

a1, b1, *c1 = [1, 2, 3, 4, 5, 6]  # list
print(a1, b1, c1)  # 1 2 [3, 4, 5, 6]

a2, b2, *c2 = range(1, 7)  # range
print(a2, b2, c2)  # 1 2 [3, 4, 5, 6]

a3, b3, *c3 = 'hello'  # string
print(a3, b3, c3)  # h e ['l', 'l', 'o']

a4, b4, *c4 = {'a': 1, 'b': 2, 'c': 3, 'd': 4}.items()  # dict
print(a4, b4, c4)
# ('a', 1) ('b', 2) [('c', 3), ('d', 4)] 以元组形式保存键值对

a5, *b5, c5 = [1, 2, 3, 4, 5, 6]  # 任意位置的 * 号
print(a5, b5, c5)  # 1 [2, 3, 4, 5] 6
