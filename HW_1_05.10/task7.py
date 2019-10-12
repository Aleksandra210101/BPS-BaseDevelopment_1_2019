"""
Creator: Aleksandra Krylova
"""

while True:
    DICTIONARY = {"{": "}", "[": "]", "(": ")"}
    N = int(input())
    CHECK = 1
    for i in range(0, N):
        STRING = list(input('Введите строку'))
        if len(STRING) % 2 != 0:
            CHECK = 0
            break
        try:
            for k in range(0, int(len(STRING)/2)):
                if STRING[len(STRING)-k-1] != DICTIONARY[STRING[k]]:
                    CHECK = 0
                    break
        except:
            CHECK = 0
        if CHECK == 1:
            print("yes")
        else:
            print("no")
