#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 要生成list [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]可以用list(range(1, 11))
import os

a = list(range(1, 11))
print(a)

# 生成[1x1, 2x2, 3x3, ..., 10x10]
b = [x * x for x in range(1, 11)]
print(b)

# for循环后面还可以加上if判断，这样我们就可以筛选出仅偶数的平方
c = [x * x for x in range(1, 11) if x % 2 == 0]
print(c)

# 还可以使用两层循环，可以生成全排列
d = [m + n for m in 'ABC' for n in 'XYZ']
print(d)

# 列出当前目录下的所有文件和目录名，可以通过一行代码实现：
e = [d for d in os.listdir('.')]
print(e)

f = {'x': 'A', 'y': 'B', 'z': 'C'}
print([k + '=' + v for k, v in f.items()])

# list中所有的字符串变成小写
L = ['Hello', 'World', 'IBM', 'Apple']
print([s.lower() for s in L])

L1 = ['Hello', 'World', 18, 'Apple', None]
print([m.lower() for m in L1 if isinstance(m, str)])
