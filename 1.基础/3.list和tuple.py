#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# list
c = ['a', 'b', 'c', 'd']
print("list大小", len(c))
print(c)
print(c[0])
print('最后一个元素', c[-1])
print('倒数第二个元素', c[-2])
c.append('e')
c.append(1)
c.insert(1, 'gg')
# 删除list末尾 带参数删除制定位置 pop(i)
c.pop()
print(c)

# tuple
# 另一种有序列表叫元组：tuple
# tuple和list非常类似，但是tuple一旦初始化就不能修改

a = ()
b = (1,)
d = ('a', 'b', ['A', 'B'])
print(d[2][0])
