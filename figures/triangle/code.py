import math
a_d = 7
b_d = 2
c_d = 8

__all__ = ['triangle_perimeter', 'triangle_area']
def triangle_perimeter(a=a_d, b=b_d, c=c_d):
    return a + b + c


def triangle_area(a=a_d, b=b_d, c=c_d):
    p = triangle_perimeter(a, b, c) / 2
    return math.sqrt(p * (p - a) * (p - b) * (p - c))
