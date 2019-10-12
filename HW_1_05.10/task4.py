"""
Creator: Aleksandra Krylova
"""

while True:
    COOR = []
    HIT = False
    for i in range(8):
        COOR.append(input())
    for i in range(8):
        for k in range(i+1, 8):
            if COOR[i][0] == COOR[k][0] or COOR[i][2] == COOR[k][2]:
                if abs(int(COOR[i][0])-int(COOR[k][0])) == abs(int(COOR[i][2])-int(COOR[k][2])):
                    HIT = True
    if HIT:
        print("YESSSS!")
    else:
        print("No no")
            