"""
Creator: Aleksandra Krylova
"""

while True:
    string = list(input("Введите строку: ").lower())
    string.sort()
    dictionary = {}
    for s in string:
        if s.isalpha():
            try:
                dictionary[s] += 1
            except:
                dictionary[s] = 1
    list_d = list(dictionary.items())
    list_d.sort(reverse=True, key=lambda i: i[1])
    for i in list_d:
        print(i[0], ":", i[1])
    

    
