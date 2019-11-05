#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Even Fibonacci numbers


def fibonacci(num):
    a, b = 1, 2
    if num == 1:
        return a
    elif num == 2:
        return b
    elif num < 1:
        return print("error")
    else:
        l = [a, b]
        while max(l) < num:
            n = a + b
            l.append(n)
            a, b = b, n
            num += 1
        return sum([x for x in l if x % 2 == 0])


print(fibonacci(4000000))
