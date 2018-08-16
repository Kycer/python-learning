#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import operator as op

print('包含中文的str')

# ord()函数获取字符的整数表示
# chr()函数把编码转换为对应的字符
print(ord('A'))
print(chr(66))
print(chr(25991))

# 十六进制
print('\u4e2d\u6587')

# bytes
x = b'ABCDE'
print(x)
# str通过encode()方法可以编码为指定的bytes
print('ABC'.encode('utf-8'))
print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))
# print(b'\xe4\xb8\xad\xff'.decode('utf-8'))  如果bytes中包含无法解码的字节，decode()方法会报错
print(b'\xe4\xb8\xad\xff'.decode('utf-8', errors='ignore'))

# 计算str包含多少个字符
print(len('abc'))

# 占位符
'''
占位符	替换内容
%d	整数
%f	浮点数
%s	字符串
%x	十六进制整数
'''
print('%2d-%02d' % (3, 1))
print('%.2f' % 3.1415926)
print('Age: %s. Gender: %s' % (25, True))

# 字符串格式化
print('Hello, {0}, Age: {1}'.format('Python', 18))

# 去空格及特殊符号
s = ' abcd efg hijk,lmn ,'
print(s)
print(s.strip())
print(s.lstrip())
print(s.rstrip())
print(s.strip().lstrip().rstrip(','))

# 复制字符串
str1 = 'strcpy'
str2 = str1
str1 = 'strcpy2'
print(str2)

# 查找字符
s1 = 'strchr'
s2 = 't'
nPos = s1.index(s2)
print(nPos)

# 比较字符串
str4 = 'strchr'
str2 = 'strch'
print(str4 == str2)
print(op.eq("a", "a"))

# 截取字符串
str3 = '0123456789'
print(str3[0:3])  # 截取第一位到第三位的字符
print(str3[:])  # 截取字符串的全部字符
print(str3[6:])  # 截取第七个字符到结尾
print(str3[:-3])  # 截取从头开始到倒数第三个字符之前
print(str3[2])  # 截取第三个字符
print(str3[-1])  # 截取倒数第一个字符
print(str3[::-1])  # 创造一个与原字符串顺序相反的字符串
print(str3[-3:-1])  # 截取倒数第三位与倒数第一位之前的字符
print(str3[-3:])  # 截取倒数第三位到结尾
print(str3[:-5:-3])  # 逆向截取，倒数第一位与倒数第五位之间的字符，步长为3
