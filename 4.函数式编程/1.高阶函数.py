#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 函数本身也可以赋值给变量，即：变量可以指向函数。
# 函数名其实就是指向函数的变量
# 既然变量可以指向函数，函数的参数能接收变量，
# 那么一个函数就可以接收另一个函数作为参数，这种函数就称之为高阶函数。
from functools import reduce


# map
def f(x):
    return x * x


r = list(map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(r)
print(list(map(lambda x: pow(x, 2), [1, 2, 3, 4, 5, 6, 7, 8, 9])))


# reduce
def add(a, b):
    return a + b


print(reduce(add, [1, 3, 5, 7, 9]))
print(reduce(lambda a, b: a + b, [1, 3, 5, 7, 9]))


# filter
def is_odd(n):
    return n % 2 == 1


odd = list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15]))
print(odd)
print(list(filter(lambda n: (n % 2 == 1), [1, 2, 4, 5, 6, 9, 10, 15])))

# sorted
print(sorted([36, 5, -12, 9, -21]))
print(sorted([36, 5, -12, 9, -21], key=abs))
print(sorted([36, 5, -12, 9, -21], key=lambda x: abs(x)))
