#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# __slots__我们已经知道怎么用了，__len__()方法我们也知道是为了能让class作用于len()函数。

# __str__
class S1(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'S1 object (name: %s)' % self.name

    __repr__ = __str__


print(S1("tom"))
s1 = S1("tom2")
print(s1)


# 2. __iter__
class S2(object):
    def __init__(self, name, age):
        self.name, self.age = name, age

    def __str__(self):
        return 'S1 object (name: %s)' % self.name

    __repr__ = __str__

    def __iter__(self):
        return self  # 实例本身就是迭代对象，故返回自己

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b  # 计算下一个值
        if self.a > 100000:  # 退出循环的条件
            raise StopIteration()
        return self.a  # 返回下一个值
