"""
Creator: Aleksandra Krylova
"""

while True:
    N = int(input("Количество посещенных планет: "))
    PLANNUM = {}
    PLANET = input().split(" ")
    for i in range(0, N):
        PLANNUM[PLANET[i]] = N-i
    print(sorted(PLANNUM, key=PLANNUM.__getitem__)[-1])
 