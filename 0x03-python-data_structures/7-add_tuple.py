#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    num1 = tuple_a[0] if len(tuple_a) > 0 else 0
    num2 = tuple_a[1] if len(tuple_a) > 1 else 0
    num3 = tuple_b[0] if len(tuple_b) > 0 else 0
    num4 = tuple_b[1] if len(tuple_b) > 1 else 0
    return (num1 + num3, num2 + num4)
