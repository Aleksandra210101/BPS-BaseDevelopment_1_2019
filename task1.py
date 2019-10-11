"""
Creator: Aleksandra Krylova
"""

while True:
    message = input()
    print(len(message)*23/100 + ' р. ' + (len(message) * 23 % 100) + ' коп. ')