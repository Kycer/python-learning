#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Animal(object):
    @staticmethod
    def run():
        print('Animal is running...')


class Dog(Animal):

    @staticmethod
    def run():
        print('Dog is running...')


class Cat(Animal):
    pass


dog = Dog()
dog.run()
print(isinstance(dog, Animal))

cat = Cat()
cat.run()
