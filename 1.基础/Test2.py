# 九九乘法表
i = 1
while i <= 9:
    j = 1
    while j <= i:
        print("%d*%d=%d" % (j, i, (j * i)), end='\t')
        j += 1
    print()
    i += 1

print("\n\n")

for i in range(1, 10):
    for j in range(1, i + 1):
        print("%d*%d=%d" % (j, i, (j * i)), end='\t')
    print()

