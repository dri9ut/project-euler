#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Largest prime factor


def factor(num):
    arr = [x for x in range(2, num)]
    i = 0
    while arr[i] < num:
        for x in arr:
            if x % i == 0:
                arr.remove(x)
        i += 1
    return arr


print(factor(13195))
