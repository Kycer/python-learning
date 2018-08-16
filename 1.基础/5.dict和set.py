#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# dict全称dictionary，在其他语言中也称为map，
# 使用键-值（key-value）存储，具有极快的查找速度。

d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print(d['Michael'])

# 一是通过in判断key是否存在
print('Bob' in d)

# 通过dict提供的get()方法，如果key不存在，可以返回None，或者自己指定的value：
print(d.get('Thomas'))
print(d.get('Thomas', -1))

# set和dict类似，也是一组key的集合，但不存储value。
# 由于key不能重复，所以，在set中，没有重复的key。
s = set([1, 1, 2, 2, 3, 3])
print(s)
