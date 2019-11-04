#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Multiples of 3 and 5


def multiples(interval):
    return sum([x for x in range(1, interval) if x % 3 == 0 or x % 5 == 0])


print(multiples(1000))
