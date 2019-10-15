"""
Creator: Aleksandra Krylova
"""

while True:
    N = int(input())
    CHECK = 0
    for i in range(N):
        PHRASE = input().lower()
        PHRASE = (''.join(x for x in PHRASE if x.isalpha() or x == " ")).replace(" ", "")
        for k in enumerate(PHRASE):
            if PHRASE[k] != PHRASE[-(k+1)]:
                if i % 2 == 0:
                    print("Сослан на Плутон Юра")
                    CHECK = 1
                    break
                else:
                    print("Сослан на Плутон собеседник")
                    CHECK = 1
                    break
    if CHECK == 0:
        print("Сослать обоих")
