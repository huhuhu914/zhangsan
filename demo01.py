# print的意思是打印,print()打印括号中的所有内容。
# python 中常见的数据类型：字符串str""、整数int、小数float、布尔值bool、元组tuple()、数组list[]、字典dict{}、空Nonetype
# 数据转换的归路：除了空任何数据结构都可以转换成字符串，整数和小数可以互相转换，
# 字符串转换成其他数据类型的数据需要满足一个条件：长得像
# print同时打印多个值可以直接用逗号隔开
# print("hello world!")
# print(23333)
# print(2.333)
# print(True)
# print(())
# 字符串的拼接,只能是同类型的数据
# print("aaaaa"+"bbbbb")
# python的运算符+-*/%  python的逻辑符号and or
# print(1+5+9*9)
# 布尔值一般用于判断中
# print(2>3)


# 变量和赋值，变量必须是小写字母
# a = "张三" 把张三这个值赋值给了a这个变量
# print(a)
# input 输入,不管你输入的是什么数据类型，只要是input 方法获取的，对于代码来说都是字符串类型
# a = input("请输入：")
# b = input("请输入：")
# print("结果：",a+b)
# 数据格式的转换type,len()用于获取字符串的长度，适用于字符串、元组、数组、字典

# a=float(input("请输入数据a："))
# b=float(input("请输入数据b："))

# print("结果为：",a+b)
a=input("请输入第一段内容：")
b=input("请输入第二段内容：")
c=len(a)+len(b)
print("两段内容的总长度为：",c)