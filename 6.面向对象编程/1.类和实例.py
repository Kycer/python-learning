#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# (object)，表示该类是从哪个类继承下来的
class Student(object):
    pass


tom = Student()
tom.name = 'Tom'
print(tom)
print(tom.name)


class Teacher(object):
    # 通过定义一个特殊的__init__方法，在创建实例的时候，就把name，score等属性绑上去
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_info(self):
        print('姓名：%s，年龄：%s' % (self.name, self.age))


teacher = Teacher('AA', 23)
teacher.print_info()
