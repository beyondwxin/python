#!/usr/bin/python3

# def area(width, height):
#     '''计算那个面积'''
#     return width + height

# def print_welcome(name):
#     '''名字'''
#     print("welcome", name)

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

import sys


def fab(max):
    n = 0
    L = []
    while n < max:
        L.append(n)
        n = n + 2
    return L


f = iter(fab(10))

while True:
    try:
        print(next(f), end='\n')
    except StopIteration:
        sys.exit()
