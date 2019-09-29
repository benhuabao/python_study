"""
version:0.1
Author:wanglinag
"""
a = 10
b = 3
a += b # 相当于：a = a + b.a=13
a *= a + 2 # 相当于：a = a * (a + 2) a=13*15
print(a) # 想想这里会输出什么.a=

flag0 = 1 == 1 # true
flag1 = 3 > 2  # true
flag2 = 2 < 1  # false
flag3 = flag1 and flag2 # false
flag4 = flag1 or flag2 # true
flag5 = not (1 != 2) # true
print('flag0 =', flag0) # flag0 = True
print('flag1 =', flag1) # flag1 = True
print('flag2 =', flag2) # flag2 = False
print('flag3 =', flag3) # flag3 = False
print('flag4 =', flag4) # flag4 = True
print('flag5 =', flag5) # flag5 = False
print(flag1 is True) # True
print(flag2 is not False) # False


a = int(input("a = "))
b = int(input("b = "))
print("%d + %d = %d" % (a, b, a+b))
print('%d - %d = %d' % (a, b, a - b))
print('%d * %d = %d' % (a, b, a * b))
print('%d / %d = %f' % (a, b, a / b))
print('%d // %d = %d' % (a, b, a // b))
print('%d %% %d = %d' % (a, b, a % b))
print('%d ** %d = %d' % (a, b, a ** b))

