#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# 计算阶乘n! = 1 x 2 x 3 x ... x n
def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)


print(fact(1))
print(fact(5))
print(fact(100))
