#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Power digits sum


def digit(num):
    return sum([int(x) for x in str(num)])


print(digit(pow(2, 1000)))
