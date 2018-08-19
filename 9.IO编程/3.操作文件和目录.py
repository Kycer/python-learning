#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os

# 如果是posix，说明系统是Linux、Unix或Mac OS X，如果是nt，就是Windows系统
# uname()函数在Windows上不提供
print('操作系统名称： %s, 详细信息： %s' % (os.name, os.uname()))
print('环境变量： %s, PATH值： %s' % (os.environ, os.environ.get('PATH')))

# 操作文件和目录
print('当前目录的绝对路径: %s' % (os.path.abspath('.'),))
# 在某个目录下创建一个新目录，首先把新目录的完整路径表示出来:
test = os.path.join(os.path.abspath('.'), 'test')
print(test)
if os.path.exists(test):
    # 删掉一个目录:
    os.rmdir(test)
    # 然后创建一个目录:
    os.mkdir(test)
    # 删掉一个目录:
    os.rmdir(test)

# 把两个路径合成一个时，不要直接拼字符串，而要通过os.path.join()函数
# 要拆分路径时，也不要直接去拆字符串，而要通过os.path.split()函数


# 对文件重命名: os.rename
# 删掉文件: os.remove


# 但是复制文件的函数居然在os模块中不存在！原因是复制文件并非由操作系统提供的系统调用。理论上讲，我们通过上一节的读写文件可以完成文件复制，只不过要多写很多代码。
# 幸运的是shutil模块提供了copyfile()的函数，你还可以在shutil模块中找到很多实用函数，它们可以看做是os模块的补充。


# 列出当前目录下的所有目录
print([x for x in os.listdir('.') if os.path.isdir(x)])
# 要列出所有的.py文件
print([x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py'])