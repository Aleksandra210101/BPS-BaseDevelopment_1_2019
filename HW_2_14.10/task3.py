"""
Creator: Aleksandra Krylova
"""
import operator

CHECK = True
LANG_DICT = {}
STR_LIST = []
MID_ANSWER_LIST = []
ANSWER_LIST = []
while CHECK:
    LANGUAGE = input()
    if LANGUAGE == '':
        CHECK = False
        break
    else:
        LANG_DICT[LANGUAGE.split(" ")[0]] = LANGUAGE.split(" ")[1]
CHECK = True
while CHECK:
    STRING = input()
    if STRING == '':
        CHECK = False
        break
    else:
        STR_LIST.append(STRING.lower())
for _, i in enumerate(STR_LIST):                            # проходимся по фразам
    word_list = i.split(" ")
    for k in word_list:                                     #проходимся по словам в фразах
        mid_dict = {}
        for s in k:                                         #проходимся по буквам в словах
            for key, value in LANG_DICT.items():            #проходимся по алфавиту
                if s in LANG_DICT[key]:
                    try:
                        mid_dict[key] += 1
                    except KeyError:
                        mid_dict[key] = 1
        try:
            MID_ANSWER_LIST.append([max(mid_dict.items(), key=operator.itemgetter(1))[0]][0])
        except ValueError:
            MID_ANSWER_LIST.append(" ")
    try:
        ANSWER_LIST.append(" ".join(sorted(list(set(MID_ANSWER_LIST)))))
    except TypeError:
        ANSWER_LIST.append(MID_ANSWER_LIST)
    MID_ANSWER_LIST = []
for i in ANSWER_LIST:
    print(i)
