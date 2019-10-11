"""
Creator: Aleksandra Krylova
"""

while True:
    first_num = float(input("Введите первое число "))
    second_num = float(input("Введите второе число "))
    string = input("Введите строку ")

    if string == "+":
        print(round(first_num+second_num), 1)
    elif string == "-":
        print(round(first_num-second_num), 1)
    elif string == "/":
        if second_num == 0:
            print("ЫЫЫЫЫЫЫ")
        else:
            print(round(first_num-second_num), 1)
    elif string == "*":
        print(round(first_num*second_num), 1)
    else:
        print("ЫЫЫЫЫЫЫ")
    
    