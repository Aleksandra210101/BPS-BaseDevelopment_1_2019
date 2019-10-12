"""
Creator: Aleksandra Krylova
"""

while True:
    NUMBER = int(input("Введите число NUMBER: "))
    DIVIDER = [1]
    for i in range(2, NUMBER + 1):
        if (NUMBER % i) == 0:
            DIVIDER.append(i)
    print(" ".join(map(str, DIVIDER)))
    if len(DIVIDER) == 2:
        print("ACHTUNG")
