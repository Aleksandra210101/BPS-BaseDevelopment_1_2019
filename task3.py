"""
Creator: Aleksandra Krylova
"""


while True:
    X_START = int(input())
    Y_START = int(input())
    X_FINISH = int(input())
    Y_FINISH = int(input())
    if abs(X_START-X_FINISH) == 2 and abs(Y_START-Y_FINISH) == 5:
        print("YESSSS!")
    elif abs(X_START-X_FINISH) == 5 and abs(Y_START-Y_FINISH) == 2:
        print("YESSSS!")
    else:
        print("No no")
        