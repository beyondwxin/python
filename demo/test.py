#!/usr/bin/python3


def area(width, height):
    '''计算那个面积'''
    return width + height


def print_welcome(name):
    '''名字'''
    print("welcome", name)


print_welcome("Ruoo")
w = 4
h = 5
print("width=", w, "height=", h, area(w, h))
