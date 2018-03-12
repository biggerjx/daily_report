#!/usr/bin/env python3
# -*- coding: utf-8 -*-


'''小明身高1.75，体重80.5kg。请根据BMI公式（体重除以身高的平方）帮小明计算他的BMI指数，并根据BMI指数：
低于18.5：过轻
18.5-25：正常
25-28：过重
28-32：肥胖
高于32：严重肥胖
'''

import math


def test1():
    high = 1.75
    weight = 80.5

    BMI = weight/(high*high)
    print BMI

    if BMI <= 18.5:
        print(u"过轻")
    elif BMI <= 25:
        print(u"正常")
    elif BMI <= 28:
        print(u"过重")
    elif BMI <= 32:
        print(u"肥胖")
    else:
        print(u"严重肥胖")
    return

"""请定义一个函数quadratic(a, b, c)，接收3个参数，返回一元二次方程：
ax2 + bx + c = 0的两个解。
提示：计算平方根可以调用math.sqrt()函数
"""

def test2(a,b,c):

    if a!=0:
        r = b * b - 4 * a * c
        if r>=0:
            x1 = (-b + math.sqrt(r))/2/a
            x2 = (-b - math.sqrt(r))/(2*a)
            print x1
            print x2
        else:
            print(u"无解")
    else:
        x1 = 0
        x2 = 0

    return x1,x2

"""
杨辉三角定义如下：

          1
         / \
        1   1
       / \ / \
      1   2   1
     / \ / \ / \
    1   3   3   1
   / \ / \ / \ / \
  1   4   6   4   1
 / \ / \ / \ / \ / \
1   5   10  10  5   1
把每一行看做一个list，试写一个generator，不断输出下一行的list：
# 期待输出:
# [1]
# [1, 1]
# [1, 2, 1]
# [1, 3, 3, 1]

1, 1, 2, 3, 5, 8, 13, 21, 34, ...

def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'

"""

def test3(max):
    n = 0
    a = [1]
    b = [1,1]
    while n < max:
        if i<max :
            q = b[i-1]+b[i] #新增的数字
            b.append(q)  #追加到列表后面
            yield b
            i=i+1

        n = n + 1

def test4(max):
    a = [1]
    while True:
        yield a
        a=[x+y for x,y in (a[:-1],a[1:])]



def triangles():
    L=[1]
    while(True):
        yield L
        L=[1]+[x+y for x,y in zip(L[:-1],L[1:])]+[1]
    n = 0
    max=int(input('请输入杨辉三角的行数：'))
    for t in triangles():
        print(t)
        n = n + 1








if __name__ == '__main__':

    #test1()
    test3(3)
    triangles


