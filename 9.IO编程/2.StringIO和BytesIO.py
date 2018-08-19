#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# 很多时候，数据读写不一定是文件，也可以在内存中读写。
# StringIO和BytesIO是在内存中操作str和bytes的方法，使得和读写文件具有一致的接口。
from io import StringIO, BytesIO

f = StringIO()
f.write('hello')
f.write(' ')
f.write('world!')
f.writelines("test1")
f.writelines("test2")
print(f.getvalue())

f2 = StringIO('Hello!\nHi!\nGoodbye!')
while True:
    s = f2.readline()
    if s == '':
        break
    print(s.strip())

fw = BytesIO()
fw.write('中文'.encode('utf-8'))
print(fw.getvalue())

fw2 = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
print(fw2.read())
