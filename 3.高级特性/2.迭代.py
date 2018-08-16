#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from collections import Iterable

d = {'a': 1, 'b': 2, 'c': 3}
for key in d:
    print(key)
for value in d.values():
    print(value)
for k, v in d.items():
    print(k, v)

# str是否可迭代 True
print(isinstance('abc', Iterable))
# list是否可迭代 True
print(isinstance([1, 2, 3], Iterable))
# 整数是否可迭代 False
print(isinstance(123, Iterable))


# Python内置的enumerate函数可以把一个list变成索引-元素对
for i, value in enumerate(['A', 'B', 'C']):
    print(i, value)

# for循环里，同时引用了两个变量
for x, y in [(1, 1), (2, 4), (3, 9)]:
    print(x, y)
