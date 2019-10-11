"""
Creator: Aleksandra Krylova
"""
from math import gcd


while True:
    n = int(input())
    numerator = []
    divider = []
    sum_num = 0
    div = 1
    for i in range(0, n):
        numerator.append(int(input("Числитель:")))
        divider.append(int(input("Знаменатель:")))
    for i in range(0, n):
        div = div * divider[i]
    for i in range(0, n-1):
        gcd1 = gcd(divider[i], divider[i+1])
    for i in range(0, n):
        numerator[i] = numerator[i]*div/divider[i]
        sum_num += numerator[i]

    print(str(round(round(sum_num) / gcd(round(sum_num), div))) + '/' + str(round(div / gcd(round(sum_num), div))))