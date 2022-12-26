from termcolor import cprint, colored  # Для изменения цвета текста
import time  # Для пауз в анимации
import random  # Для генерации выпадения чисел

# ======================================================

currency = "руб"  # Выбранная денежная единица
money = 0  # Текущее количество денег
start_money = 0  # Количество денег при старте программы
play_game = True  # Продолжается ли игра?
default_money = 10000  # Количество денег по умолчанию

# =====================================================


def win(result):
    """Вывод сообщения о проигрыше"""
    cprint(f" Победа за тобой! Выигрыш составил: {result} {currency}", color(2))
    cprint(f" У тебя на счету: {money} {currency}", color(2))


def lose(result):
    """Вывод сообщения о проигрыше"""
    cprint(f" К сожалению, проигрыш: {result} {currency}", color(1))
    cprint(f" У тебя на счету: {money} {currency}", color(1))
    cprint(" Обязательно нужно отыграться!", color(1))


def get_max_count(digit, v1, v2, v3, v4, v5):
    """Считает количество совпадений"""
    counter = 0
    if digit == v1:
        counter += 1
    if digit == v2:
        counter += 1
    if digit == v3:
        counter += 1
    if digit == v4:
        counter += 1
    if digit == v5:
        counter += 1
    return counter


def get_OHB_res(bet):
    """Анимация вращения"""
    result = bet

    # Создаем переменные для каждого числа
    d1 = 0
    d2 = 0
    d3 = 0
    d4 = 0
    d5 = 0

    # Создаём флаги для каждого числа
    get_d1 = True
    get_d2 = True
    get_d3 = True
    get_d4 = True
    get_d5 = True

    # Условия
    while get_d1 or get_d2 or get_d3 or get_d4 or get_d5:
        if get_d1:
            d1 += 1
        if get_d2:
            d2 -= 1
        if get_d3:
            d3 += 1
        if get_d4:
            d4 -= 1
        if get_d5:
            d5 += 1

        if d1 > 9:
            d1 = 0
        if d2 < 0:
            d2 = 9
        if d3 > 9:
            d3 = 0
        if d4 < 0:
            d4 = 9
        if d5 > 0:
            d5 = 0

        if random.randint(0, 20) == 1:
            get_d1 = False
        if random.randint(0, 20) == 1:
            get_d2 = False
        if random.randint(0, 20) == 1:
            get_d3 = False
        if random.randint(0, 20) == 1:
            get_d4 = False
        if random.randint(0, 20) == 1:
            get_d5 = False

        # Оформление анимации
        time.sleep(0.1)
        cprint("     " + "%" * 10, color(7))
        cprint(f"     {d1} {d2} {d3} {d4} {d5}", color(7))

    # Считаем совпадения
    max_count = get_max_count(d1, d1, d2, d3, d4, d5)

    if max_count < get_max_count(d2, d1, d2, d3, d4, d5):
        max_count = get_max_count(d2, d1, d2, d3, d4, d5)
    if max_count < get_max_count(d3, d1, d2, d3, d4, d5):
        max_count = get_max_count(d2, d1, d2, d3, d4, d5)
    if max_count < get_max_count(d4, d1, d2, d3, d4, d5):
        max_count = get_max_count(d2, d1, d2, d3, d4, d5)
    if max_count < get_max_count(d5, d1, d2, d3, d4, d5):
        max_count = get_max_count(d2, d1, d2, d3, d4, d5)

    # Вывод сообщения о выигрыше или проигрыше
    if max_count == 2:
        cprint(f" Совпадение двух чисел! Твой выигрыш в размере ставки: {result}", color(7))
    elif max_count == 3:
        result *= 2
        cprint(f" Совпадение рех чисел! Твой выигрыш 2:1: {result}", color(2))
    elif max_count == 4:
        result *= 5
        cprint(f" Совпадение ЧЕТЫРЕХ чисел! Твой выигрыш 5:1: {result}", color(2))
    elif max_count == 5:
        result *= 10
        cprint(f" БИНГО! Совпадение ВСЕХ чисел! Твой выигрыш 10:1: {result}", color(2))
    else:
        lose(result)
        result = 0

    # Задерживаем экран для ознакомления пользователя с результатом
    print()
    input(" Нажмите Enter для продолжения...")

    # Возвращаем результат
    return result


def one_hand_bandit():
    """Однорукий бандит"""
    # Подгружаем количество денег и ставим флаг
    global money
    play_game = True

    # Главный цикл
    while play_game:
        # Приветствие
        color_line(2, "ДОБРО ПОЖАЛОВАТЬ НА ИГРУ В ОДНОРУКОГО БАНДИТА!")
        cprint(f" У тебя на счету {money} {currency}\n", color(3))
        cprint(" Правила игры: ", color(3))
        cprint("     1. При совпадении 2-х чисел ставка не списывается.", color(3))
        cprint("     2. При совпадении 3-х чисел выигрыш 2:1.", color(3))
        cprint("     3. При совпадении 4-х чисел выигрыш 5:1.", color(3))
        cprint("     4. При совпадении 5-ти чисел выигрыш 10:1.", color(3))
        cprint("     0. Ставка 0 для завершения игры\n", color(3))

        # Выбор ставки
        bet = get_int_input(0, money, f"     Введи ставку от 0 до {money}: ")
        if bet == 0:
            return 0

        # Отображаем исход вращения на балансе
        money -= bet
        money += get_OHB_res(bet)

        if money <= 0:
            play_game = False



def get_dice():
    """Анимация костей"""
    count = random.randint(3, 8)  # Сколько раз будут меняться числа на кубиках
    sleep = 0  # Пауза

    # Анимация
    while count > 0:
        x = random.randint(1, 6)  # Первый кубик
        y = random.randint(1, 6)  # Второй кубик
        cprint(" " * 10 + " ----- -----", color(7))
        cprint(" " * 10 + f" | {x} | | {y} |", color(7))
        cprint(" " * 10 + " ----- -----", color(7))
        time.sleep(sleep)
        sleep += 1 / count
        count -= 1

    # Возвращаем сумму выпавших кубов
    return x + y


def dice():
    """Кости"""
    # Подгружаем количество денег и ставим флаг
    global money
    play_game = True

    # Главный цикл
    while play_game:
        # Приветствие
        color_line(2, "ДОБРО ПОЖАЛОВАТЬ НА ИГРУ В КОСТИ!")
        cprint(f" У тебя на счету {money} {currency}\n", color(3))

        # Выбор ставки
        bet = get_int_input(0, money, f"     Сделай ставку в пределах {money} {currency} (0 - для выхода): ")
        if bet == 0:
            return 0

        play_round = True  # Игровой цикл
        control = bet  # Ставка пользователя
        old_result = get_dice()  # Старое значение костей
        first_play = True  # Проверка на первый раунд

        # Главный цикл
        while play_round and bet > 0 and money > 0:
            # Проверка на превышение баланса
            if bet > money:
                bet = money

            # Приглашение
            cprint(f"\n     В твоем распоряжении {bet} {currency}", color(3))
            cprint(f"\n     Текущая сумма чисел на костях: {old_result}", color(3))
            cprint("\n     Сумма чисел на гранях будет больше, меньше или равна предыдущей?")

            x = get_input("0123", "     Введи 1 - больше, 2 - меньше, 3 - равна или 0 - выход: ")

            # Игра
            if x != "0":
                first_play = False
                if bet > money:
                    bet = money

                money -= bet

                # Получаем бросок
                dice_result = get_dice()

                # Проверяем выбор пользователя
                user_win = False
                if old_result > dice_result:
                    if x == "2":
                        user_win = True
                elif old_result < dice_result:
                    if x == "1":
                        user_win = True
                if x != "3":
                    if user_win:
                        money += bet + bet // 5
                        win(bet // 5)
                        bet += bet // 5
                    else:
                        bet = control
                        lose(bet)
                elif x == "3":
                    if old_result == dice_result:
                        money += bet * 3
                        win(bet * 2)
                        bet *= 3
                    else:
                        bet = control
                        lose(bet)

                # Приравниваем нынешний результат к предыдущему для следующего раунда
                old_result = dice_result

            # Выход
            else:
                if first_play:
                    money -= bet
                play_round = False


def get_roulette(visible):
    """Анимация рулетки"""
    tick_time = random.randint(100, 200) / 10000  # Определяем время, на которое будет увеличиваться пауза
    main_time = 0  # Пауза в секундах
    number = random.randint(0, 38)  # Выпавший номер на рулетке
    increase_tick_time = random.randint(100, 110) / 100  # Определяем время, на которое будет увеличиваться tick_time

    # Пока пауза меньше 0.7
    while main_time < 0.7:
        # Увеличение времени паузы
        main_time += tick_time
        tick_time *= increase_tick_time

        # Увеличение номера
        number += 1
        if number > 38:
            number = 0
            print()

        # Обработка "00" и "000"
        print_number = number
        if number == 37:
            print_number = "00"
        elif number == 38:
            print_number = "000"

        # Вывод числа
        # print(" Число >", print_number, "*" * number, " " * (79 - number * 2), "*" * number)
        cprint(f" Число > {print_number} {'*' * number} {' ' * (79 - number * 2)} {'*' * number}", color(7))

        # Пауза
        if visible:
            time.sleep(main_time)

    # Возврат номера
    return number


def roulette():
    """Рулетка"""
    # Подгружаем количество денег и ставим флаг
    global money
    play_game = True

    # Главный цикл
    while play_game and money > 0:
        # Приветствие
        color_line(2, "ДОБРО ПОЖАЛОВАТЬ НА ИГРУ В РУЛЕТКУ!")
        cprint(f" У тебя на счету {money} {currency}\n", color(3))

        # Выбор ставки
        print(" Ставлю на...")
        print("     1. Четное (выигрыш 1:1)")
        print("     2. Нечетное (выигрыш 1:1)")
        print("     3. Дюжина (выигрыш 3:1)")
        print("     4. Число (выигрыш 36:1)")
        print("     0. Возврат в предыдущее меню")

        x = get_input("01234", "     Твой выбор? ")

        play_roulette = True

        # Выбор диапазона в дюжине
        if x == "3":
            print("Выбери числа:...")
            print("     1. От 1 до 12")
            print("     2. От 13 до 24")
            print("     3. От 25 до 36")
            print("     0. Назад")

            dozens = get_input("0123", "     Твой выбор? ")

            if dozens == "1":
                text_dozens = "от 1 до 12"
            elif dozens == "2":
                text_dozens = "от 13 до 24"
            elif dozens == "3":
                text_dozens = "от 25 до 36"
            elif dozens == "0":
                play_roulette = False

        # Выбор числа
        elif x == "4":
            number = get_int_input(0, 36, "     На какое число ставить? (0..36): ")

        # Выход
        if x == "0":
            return 0

        # Игра
        if play_roulette:
            # Запрашиваем ставку (если ставка == 0, выход)
            bet = get_int_input(0, money, f"     Сколько поставишь? (не больше {money}): ")
            if bet == 0:
                return 0

            # Получение числа
            number_roulette = get_roulette(True)

            # Выводим полученное число
            print()
            if number_roulette < 37:
                cprint(f"     Выпало число {number_roulette}! " + "*" * number_roulette, color(7))
            else:
                if number_roulette == 37:
                    print_number = "00"
                elif number_roulette == 38:
                    print_number = "000"
                cprint(f"     Выпало число {print_number}!", color(7))

            # Проверка ставки и результата
            # Четное
            if x == "1":
                print("     Ты ставил на ЧЕТНОЕ!")
                if number_roulette < 37 and number_roulette % 2 == 0:
                    money += bet
                    win(bet)
                else:
                    money -= bet
                    lose(bet)
            # Нечетное
            elif x == "2":
                print("     Ты ставил на НЕЧЕТНОЕ!")
                if number_roulette < 37 and number_roulette % 2 != 0:
                    money += bet
                    win(bet)
                else:
                    money -= bet
                    lose(bet)
            # Дюжина
            elif x == "3":
                print(f"     Ставка сделана на диапазон чисел {text_dozens}.")

                win_dozens = ""  # Переменная для сравнения выигравшей дюжины
                if number_roulette > 0 and number_roulette < 13:
                    win_dozens = "1"
                elif number_roulette > 12 and number_roulette < 25:
                    win_dozens = "2"
                elif number_roulette > 24 and number_roulette < 37:
                    win_dozens = "3"

                if dozens == win_dozens:
                    money += bet * 2
                    win(bet * 3)
                else:
                    money -= bet
                    lose(bet)
            # Число
            elif x == "4":
                print(f"     Ставка сделана на число {number}")
                if number_roulette == number:
                    money += bet * 35
                    win(bet * 36)
                else:
                    money -= bet
                    lose(bet)

            # Задерживаем экран для ознакомления пользователя с результатом
            print()
            input(" Нажмите Enter для продолжения...")



def load_money():
    """Загрузка оставшейся суммы из файла"""
    try:
        with open("money.dat") as f:
            m = int(f.readline())
    except FileNotFoundError:
        print(f"Текущее значение не обнаружено, задано значение {default_money} {currency}")
        m = default_money
    return m


def save_money(money_to_save):
    """Запись суммы в файл"""
    try:
        with open("money.dat", "w") as f:
            f.write(str(money_to_save))
    except:
        print("Ошибка сохранения, наше Казино закрывается!")
        quit(0)


def color(col):
    """Установка цвета текста"""
    colors = {0: "grey", 1: "red", 2: "green", 3: "yellow", 4: "blue", 5: "magenta", 6: "cyan", 7: "white"}
    return colors[col]


def color_line(col, text):
    """Вывод на экран цветного, очищенного сверху, обрамленного текста"""
    for i in range(30):
        print()
    cprint("*" * (len(text) + 2), color(col))
    cprint(" " + text, color(col))
    cprint("*" * (len(text) + 2), color(col))


def get_int_input(minimum, maximum, message):
    """Ввод целочисленного значения от пользователя"""
    select = -1
    while select < minimum or select > maximum:
        # print(colored(message, color(7)), end="")  # Если нужно сделать цветной вопрос (надо удалить message снизу)
        inp = input(message)
        if inp.isdigit():
            select = int(inp)
        else:
            cprint("     Введи целое число!", color(1))
    return select


def get_input(digit, message):
    """Выбор пункта меню"""
    select = ""
    while select == "" or select not in digit:
        # print(colored(message, color(7)), end="")  # Если нужно сделать цветной вопрос (надо удалить message снизу)
        select = input(message)
    return select


def main():
    """Главная функция"""
    global money, play_game

    # Загружаем количество денег и запоминаем начальную сумму для статистики
    money = load_money()
    start_money = money

    # Главный цикл
    while play_game and money > 0:
        # Приветствие
        color_line(2, "Приветствую тебя в нашем Казино, дружище!")
        cprint(f" У тебя на счету {money} {currency}", color(4))

        # Отображение меню
        cprint(" Ты можешь сыграть в", color(6))
        cprint("     1. Рулетку", color(6))
        cprint("     2. Кости", color(6))
        cprint("     3. Однорукого бандита", color(6))
        cprint("     0. Выход. Ставка 0 в играх - выход.", color(6))

        # Выбор пользователя
        x = get_input("0123", "     Твой выбор? ")

        # Проверка выбора пользователя
        if x == "0":
            play_game = False
        elif x == "1":
            roulette()
        elif x == "2":
            dice()
        elif x == "3":
            one_hand_bandit()

    # Выход из программы
    color_line(3, "Жаль, что ты покидаешь нас! Но возвращайся скорей!")
    # Вывод сообщения в случае, если закончились деньги
    if money <= 0:
        cprint(" Упс, ты остался без денег. Возьми микрозайм и возвращайся!", color(4))

    # Вывод в случае, если пользователь увеличил банк
    if money > start_money:
        cprint("Ну что ж, поздравляем с прибылью!", color(5))
        cprint(f"На начало игры у тебя было {start_money} {currency}", color(5))
        cprint(f"Сейчас уже {money} {currency}! Играй и приумножай!")
    # Вывод в случае, если пользователь уменьшил банк
    else:
        cprint(f"К сожалению, ты проиграл {start_money - money} {currency}", color(5))
        cprint("В следующий раз все обязательно получится!")

    # Сохраняем оставшуюся сумму пользователя в файл и выходим
    save_money(money)
    quit(0)


main()
