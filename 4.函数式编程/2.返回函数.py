#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# 函数作为返回值

# 通常情况下，求和的函数是这样定义的：
def calc_sum(*args):
    ax = 0
    for n in args:
        ax = ax + n
    return ax


# 如果不需要立刻求和，而是在后面的代码中，根据需要再计算怎么办？
# 可以不返回求和的结果，而是返回求和的函数：
def lazy_sum(*args):
    def my_sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax

    return my_sum


f = lazy_sum(1, 3, 5, 7, 9)
print(f)
print(f())


# 闭包
# 全部都是9！原因就在于返回的函数引用了变量i，但它并非立刻执行。等到3个函数都返回时，它们所引用的变量i已经变成了3，因此最终结果为9。
def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i * i

        fs.append(f)
    return fs


f1, f2, f3 = count()
print(f1())
print(f2())
print(f3())


# 返回闭包时牢记一点：返回函数不要引用任何循环变量，或者后续会发生变化的变量
def count():
    def f(j):
        def g():
            return j * j

        return g

    fs = []
    for i in range(1, 4):
        fs.append(f(i))  # f(i)立刻被执行，因此i的当前值被传入f()
    return fs


f1, f2, f3 = count()
print(f1())
print(f2())
print(f3())


def count():
    def f(j):
        def g():
            return j * j

        return g

    return list(map(lambda i: f(i), range(1, 4)))


f1, f2, f3 = count()
print(f1())
print(f2())
print(f3())
