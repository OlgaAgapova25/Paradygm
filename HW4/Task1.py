# Написать скрипт для расчета корреляции Пирсона между двумя случайными величинами

from statistics import mean
from math import *

def correl (lst1, lst2):
    avg1 = mean (lst1)
    avg2 = mean (lst2)

    def num_calc(x, y):
        num = (x - avg1)*(y - avg2)
        return num

    def denom_calc1(x):
        denom = pow(x-avg1,2)
        return denom
    def denom_calc2(x):
        denom = pow(x-avg2,2)
        return denom

    r = sum(map(num_calc, lst1, lst2))/sqrt(sum(map(denom_calc1, lst1))*sum(map(denom_calc2, lst2)))

    return r

lst1 = [1, 2, 3, 4, 5]
lst2 = [2, 4, 6, 8, 10]

print(correl(lst1, lst2))