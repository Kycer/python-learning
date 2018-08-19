#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# 变量名如果以__开头，就变成了一个私有变量（private），只有内部可以访问，外部不能访问
class Student(object):

    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def set_age(self, age):
        self.__age = age

    def print_score(self):
        print('姓名：%s，年龄：%s' % (self.__name, self.__age))


tom = Student('tom', 25)
tom.print_score()
