"""
Creator: Aleksandra Krylova
"""
from math import gcd


while True:
    N = int(input())
    NUMERATOR = []
    DIVIDER = []
    SUM_NUM = 0
    DIV = 1
    for i in range(0, N):
        NUMERATOR.append(int(input("Числитель:")))
        DIVIDER.append(int(input("Знаменатель:")))
    for i in range(0, N):
        DIV = DIV * DIVIDER[i]
    for i in range(0, N-1):
        GCD1 = gcd(DIVIDER[i], DIVIDER[i+1])
    for i in range(0, N):
        NUMERATOR[i] = NUMERATOR[i] * DIV/DIVIDER[i]
        SUM_NUM += NUMERATOR[i]
    SUM_NUM = round(SUM_NUM)
    print(str(round(SUM_NUM / gcd(SUM_NUM, DIV))), '/', str(round(DIV / gcd(SUM_NUM, DIV))), sep="")
