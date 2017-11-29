#!/usr/bin/python3
import sys
sys.path.append("E:/vs_space/demo/aa/")
import test2

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

# from test2 import print_welcome

# def printme(li, str):
#     '''关键字参数，允许函数调用时参数的顺序与声明的不一致，因为解释器能够用参数名匹配参数值'''
#     print(str, li)
#     return

# printme(str="a", li="l")


def printinfo(arg1, *vars):
    '''不定长参数'''
    print(arg1)
    for it in vars:
        print(it)


# printinfo(1, 2, 3, 4)

test2.print_welcome('sd')

# test2.printme(str="a", li="l")

# if __name__ == '__main__':
#     print('是')
# else:
#     print('不是')

# import codecs
# with codecs.open('write.txt', 'r+', 'utf-8') as f:
#     print(f.read(1024))
#     # for line in f.readlines():
#     #     print(line.strip())


def add(x):
    return x * 4


print(list(map(add, [1, 2, 3, 5])))


def isok(x):
    return x % 3 == 1


print(list(filter(isok, [2, 4, 6, 9, 6])))


def lazy_sum(*args):
    '''第一次直接返回sum函数本身，并不会走sum()流程----这种程序被称为闭包'''

    # global ax = 0

    def sum():
        '''当调用f()时sum()才被调用'''

        ax = 0
        for n in args:
            ax = ax + n
        return ax

    return sum


f = lazy_sum(1, 2, 3)
print(f())

import functools


def metric(fn):
    print('%s executed in %s ms' % (fn.__name__, 10.24))
    return fn


@metric
def add(x, y):
    return x + y


print(add(4, 5))

# def log(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kw):
#         print('call %s():' % func.__name__)
#         return func(*args, **kw)
#     return wrapper

# @log
# def now():
#     print('2015-3-25')

# now()


# def log(fun):
#     @functools.wraps(fun)
#     def wrapper(*args, **kw):
#         print("start")
#         return [fun(*args, **kw), print("end")][0]

#     return wrapper


# @log
# def test(x):
#     print(x)


# test("a")

def log(func):
    def wrapper(*args, **kw):
        print('call %s:' % func.__name__)
        return [func(*args, **kw), print('end')][0]

    return wrapper


@log
def now():
    print('2017')


now()
