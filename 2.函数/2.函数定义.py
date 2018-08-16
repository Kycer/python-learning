#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math


def test_fun(x):
    if x >= 0:
        return x
    else:
        return -1


print(test_fun(9))


# 空函数 可以用pass语句
def nop():
    pass


# 返回多个值
def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny


x, y = move(100, 100, 60, math.pi / 6)
print(x, y)


# 求一元二次方程  axx + bx + c = 0
def quadratic(a, b, c=1):
    if not all(isinstance(i, (int, float)) for i in [a, b, c]):
        raise RuntimeError('参数错误')
    if a == 0:
        return - c / b
    d = pow(b, 2) - 4 * a * c
    if d < 0:
        raise RuntimeError('该方程无解')
    elif d == 0:
        return - b / (2 * a)
    else:
        x1 = (-b + math.sqrt(d)) / (2 * a)
        x2 = (-b - math.sqrt(d)) / (2 * a)
        return x1, x2


# 测试:
print('quadratic(2, 3, 1) =', quadratic(2, 3, 1))
print('quadratic(1, 3, -4) =', quadratic(1, 3, -4))

if quadratic(2, 3, 1) != (-0.5, -1.0):
    print('测试失败')
elif quadratic(1, 3, -4) != (1.0, -4.0):
    print('测试失败')
else:
    print('测试成功')


# 默认参数
def ss(n=1):
    print(n)


# 可变参数
def cc(*numbers):
    res = 0
    for i in numbers:
        res += pow(i, 2)
    return res


print(cc(1, 2))

nums = [1, 2, 3]
print(cc(*nums))


# 关键字参数
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)


person('Michael', 30)
person('Bob', 35, city='Beijing')


# 命名关键字参数 (只接收city和job作为关键字参数)
def person(name, age, *, city, job):
    print(name, age, city, job)


person('Jack', 24, city='Beijing', job='Engineer')


# 参数组合
def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)


def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)


f1(1, 2)
f1(1, 2, c=3)
f1(1, 2, 3, 'a', 'b')
f1(1, 2, 3, 'a', 'b', x=99)
f2(1, 2, d=99, ext=None)

# 通过一个tuple和dict
args = (1, 2, 3, 4)
kw = {'d': 99, 'x': '#'}
f1(*args, **kw)

args = (1, 2, 3)
kw = {'d': 88, 'x': '#'}
f2(*args, **kw)
