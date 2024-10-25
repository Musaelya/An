numbers = [[1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 1, 1, 2, 1, 3, 1, 4, 1],
           [5, 1, 6, 1, 7, 1, 8, 1, 9]]  # здесь хранится список чисел
beginning_game = int(
    input('Добро пожаловать в игру 19.Если вы хотите продолжить игру нажмите-1 если нет,то нажмите-0: ')) #спрашиваем у пользователя хочет ли он играть
if beginning_game == 1: #и если хочет выводим правила игры
    print('Мы ради приветствовать вас в нашей игре! ')
    print('Для начало ознакомьтесть с правилами игры')
    print(
        'Правила игры: игроку необходимо вычеркнуть парные цифры или дающие в сумме 10. Условие -  пары должны находиться рядом или через зачеркнутые цифры по горизонтали или по вертикали. После того как все возможные пары вычеркнуты, оставшиеся цифры переписываются в конец таблицы. ')
    print('Цель: вычеркнуть все цифры')
    print('Удачи!')
    print()
else: #в противном случае заканчиваем игру
    print('Нам очень жаль, что вы отказались играть в нашу игру')
if beginning_game == 1:
    start = True
    while start: #создаем бесс. цикл
        for row in numbers:
            print(' '.join(map(str, row))) #выводим наш список
        coordinates_x_line = int(input('Введите номер строки для первого числа(1,3): '))   #запрашивем координаты у пользователя
        coordinates_x_column = int(input('Введите номер столбца для первого числа(1, 9): '))
        # Получение значения по координатам
        value_x = numbers[coordinates_x_line - 1][coordinates_x_column - 1] #здесь хранится координат х
        print("Значение на координатах ({}, {}): {}".format(coordinates_x_line, coordinates_x_column, value_x)) #выводим этот координат для х
        coordinates_y_line = int(input('Введите номер строки для первого числа(1,3): ')) #здесь те же самые действия для y
        coordinates_y_column = int(input('Введите номер столбца для первого числа(1, 9): '))
        # Получение значения по координатам
        value_y = numbers[coordinates_y_line - 1][coordinates_y_column - 1]
        print("Значение на координатах ({}, {}): {}".format(coordinates_y_line, coordinates_y_column, value_y))
        if value_x + value_y == 10: #если координаты в сумме дают 10, то вычеркиваем его
            numbers[coordinates_x_line - 1][coordinates_x_column - 1] = '-' #если эти координаты по проверке подошли, то вычеркиваем их
            numbers[coordinates_y_line - 1][coordinates_y_column - 1] = '-'
            print('Убираем число', value_x, 'и', value_y) #говорим пользователю, что убрали эти цифры
        elif value_x == value_y: #если эти координаты равны, то их тоже убираем
            if (coordinates_x_line == coordinates_y_line) : #смотрим в одной ли они линии это координаты
                if (abs(coordinates_x_column - coordinates_y_column) == 1): #если они в одной линии, то проверяем столбы находятся ли они рядом
                    numbers[coordinates_x_line - 1][coordinates_x_column - 1] = '-' #если под условиями подходит, то эти числа убираем
                    numbers[coordinates_y_line - 1][coordinates_y_column - 1] = '-'
                    print('Убираем число', value_x, 'и', value_y,'samelinesamenumb')
                else:
                    flag = False
                    print(coordinates_x_column, coordinates_y_column)
                    for column in range(min(coordinates_x_column, coordinates_y_column),
                                        max(coordinates_x_column, coordinates_y_column)-1): #проходимся по каждому числу, чтобы проверить вся ли строка = '-'
                        if numbers[coordinates_x_line-1][column] != '-': #и если оно под условием не подходит заканчиваем этот цикл
                            flag = True
                            break
                    if not flag: #в противном случае оно подходит под условия
                        numbers[coordinates_x_line - 1][coordinates_x_column - 1] = '-'
                        numbers[coordinates_y_line - 1][coordinates_y_column - 1] = '-'
            elif (coordinates_x_column == coordinates_y_column): #а тут проверяем по столбу и если они в разных строк(которые стоят рядом), то их убираем
                if (abs(coordinates_x_line - coordinates_y_line) == 1):
                    numbers[coordinates_x_line - 1][coordinates_x_column - 1] = '-'
                    numbers[coordinates_y_line - 1][coordinates_y_column - 1] = '-'
                else:
                    flag = False
                    for line in range(min(coordinates_x_line, coordinates_y_line),
                                      max(coordinates_x_line - 1, coordinates_y_line - 1)): #а тут проверка в одном линии, но много '-' и цифры равняются
                        if numbers[line][coordinates_x_column - 1] != '-': #и тут если под условия не подходит, то завершаем цикл
                            flag = True
                            break
                        if not flag: #а если подходят, то убираем эти числа
                            numbers[coordinates_x_line - 1][coordinates_x_column - 1] = '-'
                            numbers[coordinates_y_line - 1][coordinates_y_column - 1] = '-'
        if numbers.count('-') == 26: #завершение игры,если все числа убрали
            start = False

        else:
            print('Введены неверные координаты.')
if not start:
    print('Игра окончена')