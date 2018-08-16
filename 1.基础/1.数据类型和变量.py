# 标准数据类型6种
# Number(数字)
# String(字符串)
# List(列表)
# Tuple(元组)
# Sets(集合)
# Dict(字典)

# 不可变数据（3 个）：Number（数字）、String（字符串）、Tuple（元组）
# 可变数据（3 个）：List（列表）、Dictionary（字典）、Set（集合）
# string、list和tuple都属于sequence（序列）。


# Number(数字)
# 支持 int float bool complex(复数)
# 数值计算
print("5+3=", 5 + 3)
print("5-3=", 5 - 3)
print("5*3=", 5 * 3)
print("除法得到浮点数 2/4=", 2 / 4)
print("除法得到整数 2//4=", 2 // 4)
print("取余 10%3=", 10 % 3)
print("乘方 4**2=", 4 ** 2)
print("开方 4**0.5=", 4 ** 0.5)

# String(字符串)
# 元素是不可变的
string = "abcdefg"
print(string)
print(string[0])
print(string[0:-1])  # 从头到尾
print(string[2:])  # 从下标2开始到尾
print(string[2:4])  # 从下标2到n-1  [m,n)
print(string * 2)  # 输出2次

# list(列表)
# 元素可变的
listDemo = ["aa", 1, "bb", 2]
print(listDemo)
print(listDemo[0])  # 输出下标0
print(listDemo[2:])  # 从下标2开始到尾
print(listDemo[1:3])  # 从下标2到n-1  [m,n)
print(listDemo * 2)  # 输出2次
listDemo[0] = "替换的"
print(listDemo)  # 修改后的

# tuple(元组)
# 元素不可变的
tupleDemo = ("aa", 1, "bb", 2)
print(tupleDemo)
print(tupleDemo[0])  # 输出下标0
print(tupleDemo[2:])  # 从下标2开始到尾
print(tupleDemo[1:3])  # 从下标2到n-1  [m,n)
print(tupleDemo * 2)  # 输出2次

tup1 = ()  # 空元组
tup2 = (10,)  # 一个元素
print(tup1)
print(tup2)

# Set(集合)
# 一个无序不可重复的序列
setDemo = {"a", "b", "c"}
print("集合A ", setDemo)
# 集合可以做 交集并集差集
setDemo2 = {"a", "b"}
print("集合B ", setDemo2)
print("AB的差集 ", setDemo - setDemo2)
print("AB的并集 ", setDemo | setDemo2)
print("AB的交集 ", setDemo & setDemo2)
print("AB的不同时存在的 ", setDemo ^ setDemo2)

# 字典
dictDemo = {"tom": "90", "jerry": "75"}
print(dictDemo)
print(dictDemo["tom"])
print("keys:", dictDemo.keys())
print("values", dictDemo.values())
# 移除 key 返回value
print("移除tom ", dictDemo.pop("tom"))
print(dictDemo)

# python常用数据转换
'''
int(x [,base])  将x转换为一个整数
float(x)  将x转换到一个浮点数
complex(real [,imag]) 创建一个复数
str(x)  将对象 x 转换为字符串
repr(x)  将对象 x 转换为表达式字符串
eval(str)  用来计算在字符串中的有效Python表达式,并返回一个对象
tuple(s)  将序列 s 转换为一个元组
list(s) 将序列 s 转换为一个列表
set(s) 转换为可变集合
dict(d)  创建一个字典。d 必须是一个序列 (key,value)元组。
frozenset(s) 转换为不可变集合
chr(x)  将一个整数转换为一个字符
ord(x) 将一个字符转换为它的整数值
hex(x) 将一个整数转换为一个十六进制字符串
oct(x) 将一个整数转换为一个八进制字符串
'''

# python的注释
print("单行注释 #")
print("多行注释 单引号(3个')")
print("多行注释 双引号(3个双引号)")

# isinstance 和 type
print("isinstance判断", isinstance(4, str))
'''
type()不会认为子类是一种父类类型。
isinstance()会认为子类是一种父类类型。
class A:
    pass

class B(A):
    pass

isinstance(A(), A)  # returns True
type(A()) == A      # returns True
isinstance(B(), A)    # returns True
type(B()) == A        # returns False
'''
