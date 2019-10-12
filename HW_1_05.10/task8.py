"""
Creator: Aleksandra Krylova
"""

while True:
    STRING = list(input("Введите строку: ").lower())
    STRING.sort()
    DICTIONARY = {}
    for s in STRING:
        if s.isalpha():
            try:
                DICTIONARY[s] += 1
            except:
                DICTIONARY[s] = 1
    LIST_D = list(DICTIONARY.items())
    LIST_D.sort(reverse=True, key=lambda i: i[1])
    for i in LIST_D:
        print(i[0], ":", i[1])
    