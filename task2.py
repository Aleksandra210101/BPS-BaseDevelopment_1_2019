"""
Creator: Aleksandra Krylova
"""

while True:
    FIRST_NUM = float(input("Введите первое число "))
    SECOND_NUM = float(input("Введите второе число "))
    STRING = input("Введите строку ")

    if STRING == "+":
        print(round(FIRST_NUM+SECOND_NUM, 1))
    elif STRING == "-":
        print(round(FIRST_NUM-SECOND_NUM, 1))
    elif STRING == "/":
        if SECOND_NUM == 0:
            print("ЫЫЫЫЫЫЫ")
        else:
            print(round(FIRST_NUM-SECOND_NUM, 1))
    elif STRING == "*":
        print(round(FIRST_NUM*SECOND_NUM, 1))
    else:
        print("ЫЫЫЫЫЫЫ")
    