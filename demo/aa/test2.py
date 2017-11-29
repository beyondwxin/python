#!/usr/bin/python3

# def area(width, height):
#     '''计算那个面积'''
#     return width + height


def print_welcome(name):
    '''名字'''
    print("welcome", name)


if __name__ == '__main__':
    print_welcome('aaa')
# print_welcome("Ruoo")
# w = 4
# h = 5
# print("width=", w, "height=", h, area(w, h))

# i = 4

# def foo(x):
#     def bar():
#         print(i),

#     for i in x:
#         print(i),
#     bar()

# list = ['a', '23']
# for it in list:
#     print(it, end=',')

# import sys

# def fab(max):
#     n = 0
#     L = []
#     while n < max:
#         # L.append(n)
#         yield n
#         n = n + 2
#     return L

# for x in fab(10):
#     print(x, end='\n')

# f = iter(fab(10))

# while True:
#     try:
#         print(next(f), end='\n')
#     except StopIteration:
#         sys.exit()
import sys


def printme(li, str):
    '''关键字参数，允许函数调用时参数的顺序与声明的不一致，因为解释器能够用参数名匹配参数值'''
    print(str, li)
    return


# printme(str="a", li="l")

# def printinfo(arg1, *vars):
#     '''不定长参数'''
#     print(arg1)
#     for it in vars:
#         print(it)

# printinfo(1, 2, 3, 4)

for i in sys.argv:
    print("参数：", i)