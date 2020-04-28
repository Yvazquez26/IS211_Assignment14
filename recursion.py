#!/usr/bin/env python
# coding: utf-8

# Week 14 Assignment - Recursion


def fibonacci(n):
    """Returns the nth element in the Fibonnaci sequence."""
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def gcd(a, b):
    """Returns the greatest common divisor of two numbers."""
    while b:
        (a, b) = (b, (a % b))
    return a

def CompareTo(s1, s2):
    """Compares two strings and returns a value depending on the comparison of
    the two strings."""
    if (s1 and s2) == '':
        return 0
    elif len(s1) < len(s2):
        return len(s1) - 1
    elif len(s1) > len(s2):
        return len(s1) + 1




