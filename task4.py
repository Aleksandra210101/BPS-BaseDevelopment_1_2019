"""
Creator: Aleksandra Krylova
"""

while True:
    coor = []
    hit = False
    for i in range(8):
        coor.append(input())
    for i in range(8): 
        for k in range(i+1, 8):
            if coor[i][0] == coor[k][0] or coor[i][2] == coor[k][2] or abs(int(coor[i][0])-int(coor[k][0])) == abs(int(coor[i][2])-int(coor[k][2])):
                hit = True
    if hit:
        print("Yes")
    else:
        print("No")
            
