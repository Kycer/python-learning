a = 100
b = "python"
print(type(a))
print(type(b))
for index in range(100):
    print(index)
for index in range(200, 210):
    print(index)
c = True
while c:
    name = input("请输入用户名：")
    psd = input("请输入密码：")
    # print("用户名：%(first)s, 密码：%(second)s" % {'first': name, 'second': psd})
    print("用户名：%s, 密码：%s" % (name, psd))
    if name == 'yksoul' and psd == '111111':
        print("Ok")
        c = False
    else:
        print("Error")
