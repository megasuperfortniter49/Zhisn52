import time
import random
while True:
    print("Здравствуйте, Вас приветствует игра 'Жизнь'")
    print("Сейчас Вам будет дан выбор создания мира:")
    print("Введите 1 для рандома")
    print("Введите 2 для ввода")
    print("Введите 3 для завершения игры")
    vibor = input()
    print("Введите размер 'Мира' (Длину строки)")
    razmer = int(input())
    print("Введите количество 'Поколений' (Количество повторений)")
    kolvo_pokolen = int(input())
    print("Введите символ для обозначения 'Жизни' (Специальный символ обозначающий живую клетку)")
    simvol = input()
    stroka = list()
    while vibor != "1" and vibor != "2" and vibor != "3":
        print("Введите 1 для рандома")
        print("Введите 2 для ввода")
        print("Введите 3 для завершения игры")
        vibor = input()
    if vibor == "1":
        for i in range(razmer):
            x = random.randint(0, 2)
            if x == 0:
                stroka.append(" ")
            else:
                stroka.append(simvol)
        print(*stroka)
    elif vibor == "3":
        print("Игра окончена.")
        print("Извините за неудобства (Вам пришлось вводить ненужые данные.)")
        break
    else:
        print("Задайте генерацию 'Мира' самостоятельно")
        print("Помечание: За пустую клетку отвечает пробел, за живую клетку любой символ.")
        print("Символ живой клетки поменяется на тот, который был введен пользователем.")
        world = input()
        stroka = list(world)
    stroka2 = stroka.copy()
    for i in range(kolvo_pokolen):
        for j in range(len(stroka)):
            if j == len(stroka) - 1:
                if stroka[0] == stroka[j - 1]:
                    stroka2[j] = " "
                elif stroka[0] != stroka[j - 1]:
                    stroka2[j] = simvol
            else:
                if stroka[j - 1] == stroka[j + 1]:
                    stroka2[j] = " "
                elif stroka[j - 1] != stroka[j + 1]:
                    stroka2[j] = simvol
        stroka = stroka2.copy()
        if simvol not in stroka:
            break
        print(*stroka2)
        time.sleep(0.5)
