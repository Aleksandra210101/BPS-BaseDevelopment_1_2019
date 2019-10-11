"""
Creator: Aleksandra Krylova
"""

while True:
    number = int(input("Введите число number: "))
    divider = [1]
    for i in range (2, number+1):
        if (number % i) == 0:
             divider.append(i)
    print(" ".join(map(str,divider)))
    if len(divider) == 2:
        print("ACHTUNG")
