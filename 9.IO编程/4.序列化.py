#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Python提供了pickle模块来实现序列化。
import json
import os
import pickle

d = dict(name='Bob', age=20, score=88)

txt = 'test.txt'
f = open(txt, 'wb')
pickle.dump(d, f)
f.close()

f = open(txt, 'rb')
d = pickle.load(f)
f.close()
print(d)

if os.path.exists(txt):
    # 删除文件，可使用以下两种方法。
    os.remove(txt)

# json
print(json.dumps(d))


class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score


s = Student('Bob', 20, 88)
print(json.dumps(s, default=lambda obj: obj.__dict__))

json_str = '{"name": "Bob", "age": 20, "score": 88}'


def dict2student(d):
    return Student(d['name'], d['age'], d['score'])


print(json.loads(json_str, object_hook=dict2student))
