#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Student(object):
    def __init__(self, name, age, sex):
        self.__name = name
        self.__age = age
        self.sex = sex

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def set_age(self, age):
        self.__age = age

    def print_score(self):
        print('姓名：%s，年龄：%s' % (self.__name, self.__age))


tom = Student('tom', 23, '男')

# 使用type()
print(type(tom))

# isinstance()
print(isinstance(tom, Student))

# 如果要获得一个对象的所有属性和方法，可以使用dir()函数，
# 它返回一个包含字符串的list，比如，获得一个str对象的所有属性和方法
print(dir(tom))

# 有属性'x'吗？
print(hasattr(tom, 'sex'))

# 设置一个属性'y'
print(hasattr(tom, 'y'))
setattr(tom, 'y', 19)
print(hasattr(tom, 'y'))
print(getattr(tom, 'y'))
