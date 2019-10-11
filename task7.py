"""
Creator: Aleksandra Krylova
"""

while True:
    dictionary = {"{":"}","[":"]","(":")"}
    n = int(input())
    check = 1
    for i in range(0, n):
        string = list(input('Введите строку'))
        if len(string)%2 != 0:
            check = 0
            break
        try:
            for k in range(0, int(len(string)/2)):
                if (string[len(string)-k-1] != dictionary[string[k]]):
                    check = 0
                    break
        except:
            check = 0
        if check == 1:
            print("yes")
        else:
            print("no")


