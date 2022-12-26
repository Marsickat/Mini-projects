from tkinter import *  # Для оконного отображения
from tkinter import messagebox  # Для всплывающих окон
from tkinter import ttk  # Для выпадающего списка
from random import randint  # Для генерации случайностей


def setup_horse():
    """Установка состояния лошадей и погоды"""
    global state_01, state_02, state_03, state_04
    global weather, time_day
    global win_coeff_01, win_coeff_02, win_coeff_03, win_coeff_04
    global play_01, play_02, play_03, play_04
    global reverse_01, reverse_02, reverse_03, reverse_04
    global fast_speed_01, fast_speed_02, fast_speed_03, fast_speed_04

    # Устанавливаем окружающую среду
    weather = randint(1, 5)
    time_day = randint(1, 4)

    # Устанавливаем состояние лошадей
    state_01 = randint(1, 5)
    state_02 = randint(1, 5)
    state_03 = randint(1, 5)
    state_04 = randint(1, 5)

    # Устанавливаем коэффициенты
    win_coeff_01 = int(100 + randint(1, 30 + state_01 * 60)) / 100
    win_coeff_02 = int(100 + randint(1, 30 + state_02 * 60)) / 100
    win_coeff_03 = int(100 + randint(1, 30 + state_03 * 60)) / 100
    win_coeff_04 = int(100 + randint(1, 30 + state_04 * 60)) / 100

    # Устанавливаем маркеры
    reverse_01 = False
    reverse_02 = False
    reverse_03 = False
    reverse_04 = False

    play_01 = True
    play_02 = True
    play_03 = True
    play_04 = True

    fast_speed_01 = False
    fast_speed_02 = False
    fast_speed_03 = False
    fast_speed_04 = False


def win_round(horse):
    """Окончание раунда"""
    global x_01, x_02, x_03, x_04, money

    # Формируем строку
    res = "К финишу пришла лошадь "
    # Сколько денег выиграл пользователь
    if horse == 1:
        res += name_horse_01
        win = sum_01.get() * win_coeff_01
    elif horse == 2:
        res += name_horse_02
        win = sum_02.get() * win_coeff_02
    elif horse == 3:
        res += name_horse_03
        win = sum_03.get() * win_coeff_03
    elif horse == 4:
        res += name_horse_04
        win = sum_04.get() * win_coeff_04

    # Вывод сообщения
    if horse > 0:
        res += f"! Вы выиграли {int(win)} {currency}."
        if win > 0:
            res += "Поздравляем! Средства уже зачислены на Ваш счет!"
            insert_text(f"Этот забег принес Вам {int(win)} {currency}.")
        else:
            res += "К сожалению, Ваша лошадь была неправильной. Попробуйте еще раз!"
            insert_text("Делайте ставку! Увеличивайте прибыль!")
        messagebox.showinfo("РЕЗУЛЬТАТ", res)
    # Если ни одна лошадь не пришла к финишу
    else:
        messagebox.showinfo("Все плохо", "До финиша не дошел никто. Забег признан несостоявшимся. Все ставки возвращены.")
        insert_text("Забег признан несостоявшимся.")
        win = sum_01.get() + sum_02.get() + sum_03.get() + sum_04.get()

    # Запись выигрыша в файл
    money += win
    save_money(int(money))

    # Сброс значений
    setup_horse()

    # Сброс виджетов
    start_button["state"] = "normal"
    bet_01["state"] = "readonly"
    bet_02["state"] = "readonly"
    bet_03["state"] = "readonly"
    bet_04["state"] = "readonly"
    bet_01.current(0)
    bet_02.current(0)
    bet_03.current(0)
    bet_04.current(0)

    # Сброс координат
    x_01 = 20
    x_02 = 20
    x_03 = 20
    x_04 = 20
    horse_place_in_window()

    # Обновляем интерфейс
    refresh_combo(event_object="")
    view_weather()
    health_horse()
    insert_text(f"Ваши средства: {int(money)} {currency}.")

    # Выход из программы, если сумма  меньше 1
    if money < 1:
        messagebox.showinfo("Стоп!", "На ипподром без средств заходить нельзя!")
        quit(0)


def problem_horse():
    """Генератор случайных ситуаций"""
    global reverse_01, reverse_02, reverse_03, reverse_04
    global play_01, play_02, play_03, play_04
    global fast_speed_01, fast_speed_02, fast_speed_03, fast_speed_04

    # Выбор лошади для события
    horse = randint(1, 4)

    # Чем выше число, тем ниже вероятность
    max_rand = 10000

    # Генерация события для лошади
    if horse == 1 and play_01 == True and x_01 > 0:
        if randint(0, max_rand) < state_01 * 5:
            reverse_01 = not reverse_01
            messagebox.showinfo("Аааааа!", f"Лошадь {name_horse_01} развернулась и бежит в другую сторону!")
        elif randint(0, max_rand) < state_01 * 5:
            play_01 = False
            messagebox.showinfo("Никогда такого не было и вот опять", f"{name_horse_01} заржала и скинула жокея!")
        elif randint(0, max_rand) < state_01 * 5 and not fast_speed_01:
            messagebox.showinfo("Великолепно!", f"{name_horse_01} перестала притворяться и ускорилась!")
            fast_speed_01 = True

    if horse == 2 and play_02 == True and x_02 > 0:
        if randint(0, max_rand) < state_02 * 5:
            reverse_02 = not reverse_02
            messagebox.showinfo("Аааааа!", f"Лошадь {name_horse_02} развернулась и бежит в другую сторону!")
        elif randint(0, max_rand) < state_02 * 5:
            play_02 = False
            messagebox.showinfo("Никогда такого не было и вот опять", f"{name_horse_02} заржала и скинула жокея!")
        elif randint(0, max_rand) < state_02 * 5 and not fast_speed_02:
            messagebox.showinfo("Великолепно!", f"{name_horse_02} перестала притворяться и ускорилась!")
            fast_speed_02 = True

    if horse == 3 and play_03 == True and x_03 > 0:
        if randint(0, max_rand) < state_03 * 5:
            reverse_03 = not reverse_03
            messagebox.showinfo("Аааааа!", f"Лошадь {name_horse_03} развернулась и бежит в другую сторону!")
        elif randint(0, max_rand) < state_03 * 5:
            play_03 = False
            messagebox.showinfo("Никогда такого не было и вот опять", f"{name_horse_03} заржала и скинула жокея!")
        elif randint(0, max_rand) < state_03 * 5 and not fast_speed_03:
            messagebox.showinfo("Великолепно!", f"{name_horse_03} перестала притворяться и ускорилась!")
            fast_speed_03 = True

    if horse == 4 and play_04 == True and x_04 > 0:
        if randint(0, max_rand) < state_04 * 5:
            reverse_04 = not reverse_04
            messagebox.showinfo("Аааааа!", f"Лошадь {name_horse_04} развернулась и бежит в другую сторону!")
        elif randint(0, max_rand) < state_04 * 5:
            play_04 = False
            messagebox.showinfo("Никогда такого не было и вот опять", f"{name_horse_04} заржала и скинула жокея!")
        elif randint(0, max_rand) < state_04 * 5 and not fast_speed_04:
            messagebox.showinfo("Великолепно!", f"{name_horse_04} перестала притворяться и ускорилась!")
            fast_speed_04 = True


def get_health(name, state, win):
    """Формирует информацию о лошади"""
    # Формируем строку
    s = f"Лошадь {name} "

    # Добавляем статус здоровья
    if state == 5:
        s += "мучается несварением желудка."
    elif state == 4:
        s += "плохо спала. Подергивается веко."
    elif state == 3:
        s += "сурова и беспощадна."
    elif state == 2:
        s += "в отличном настроении, покушала хорошо."
    elif state == 1:
        s += "просто ракета!"

    # Добавляем коэффициент
    s += f" ({win}:1)"

    # Возвращаем строку
    return s


def health_horse():
    """Добавляет информацию о лошадях в информационный чат"""
    insert_text(get_health(name_horse_01, state_01, win_coeff_01))
    insert_text(get_health(name_horse_02, state_02, win_coeff_02))
    insert_text(get_health(name_horse_03, state_03, win_coeff_03))
    insert_text(get_health(name_horse_04, state_04, win_coeff_04))


def view_weather():
    """Добавляет сообщение о текущей погоде в информационный чот"""
    # Формируем строку
    s = "Сейчас на ипподроме "

    # Добавляем время суток
    if time_day == 1:
        s += "ночь, "
    elif time_day == 2:
        s += "утро, "
    elif time_day == 3:
        s += "день, "
    elif time_day == 4:
        s += "вечер, "

    # Добавляем погоду
    if weather == 1:
        s += "льет сильный дождь."
    if weather == 2:
        s += "моросит дождик."
    if weather == 3:
        s += "облачно, на горизонте тучи."
    if weather == 4:
        s += "безоблачно, ветер."
    if weather == 5:
        s += "безоблачно, прекрасная погода!"

    # Отображаем строку
    insert_text(s)

def move_horse():
    """Рассчитывает положение лошадей, организует перемещение, создает случайные ситуации"""
    global x_01, x_02, x_03, x_04

    # Генерируем случайные события
    if randint(0, 100) < 20:
        problem_horse()

    # Задаем скорость перемещения лошадей
    speed_01 = (randint(1, time_day + weather) + randint(1, int((7 - state_01)) * 3)) / randint(10, 175)
    speed_02 = (randint(1, time_day + weather) + randint(1, int((7 - state_02)) * 3)) / randint(10, 175)
    speed_03 = (randint(1, time_day + weather) + randint(1, int((7 - state_03)) * 3)) / randint(10, 175)
    speed_04 = (randint(1, time_day + weather) + randint(1, int((7 - state_04)) * 3)) / randint(10, 175)

    multiple = 3
    speed_01 *= int(randint(1, 2 + state_01)) * (1 + fast_speed_01 * multiple)
    speed_02 *= int(randint(1, 2 + state_02)) * (1 + fast_speed_02 * multiple)
    speed_03 *= int(randint(1, 2 + state_03)) * (1 + fast_speed_03 * multiple)
    speed_04 *= int(randint(1, 2 + state_04)) * (1 + fast_speed_04 * multiple)

    # Перемещаем лошадей в соответствии с маркером
    if play_01:
        if not reverse_01:
            x_01 += speed_01
        else:
            x_01 -= speed_01
    if play_02:
        if not reverse_02:
            x_02 += speed_02
        else:
            x_02 -= speed_02

    if play_03:
        if not reverse_03:
            x_03 += speed_03
        else:
            x_03 -= speed_03

    if play_04:
        if not reverse_04:
            x_04 += speed_04
        else:
            x_04 -= speed_04

    # Отображаем перемещение лошадей
    horse_place_in_window()

    # Ситуации
    all_play = play_01 or play_02 or play_03 or play_04  # Возникает ложь, когда все стоят
    all_x = x_01 < 0 and x_02 < 0 and x_03 < 0 and x_04 < 0  # Возникнет истина, когда все убегут влево экрана
    all_reverse = reverse_01 and reverse_02 and reverse_03 and reverse_04  # Возникнет истина, когда все бегут обратно

    # Проверяем ситуации
    if not all_play or all_x or all_reverse:
        win_round(0)
        return 0

    # Вызываем метод каждые 5 миллисекунд, пока какая-либо лошадь не дойдет до финиша
    if x_01 < 952 and x_02 < 952 and x_03 < 952 and x_04 < 952:
        root.after(5, move_horse)
    # Выводим победившую лошадь
    else:
        if x_01 >= 952:
            win_round(1)
        elif x_02 >= 952:
            win_round(2)
        elif x_03 >= 952:
            win_round(3)
        elif x_04 >= 952:
            win_round(4)


def run_horse():
    """Запускает забег"""
    global money

    # Отключаем изменение ставок и нажатие кнопки во время забега
    start_button["state"] = "disabled"
    bet_01["state"] = "disabled"
    bet_02["state"] = "disabled"
    bet_03["state"] = "disabled"
    bet_04["state"] = "disabled"

    # Вычитаем ставку и общей суммы пользоваетеля
    money -= sum_01.get() + sum_02.get() + sum_03.get() + sum_04.get()

    # Запускаем забег
    move_horse()


def refresh_combo(event_object):
    """Обновляет суммы для ставки"""
    total = sum_01.get() + sum_02.get() + sum_03.get() + sum_04.get()
    label_all_money["text"] = f"У вас на счету: {int(money - total)} {currency}."

    # Динамическое изменение суммы ставок
    bet_01["values"] = get_values(int(money - sum_02.get() - sum_03.get() - sum_04.get()))
    bet_02["values"] = get_values(int(money - sum_01.get() - sum_03.get() - sum_04.get()))
    bet_03["values"] = get_values(int(money - sum_01.get() - sum_02.get() - sum_04.get()))
    bet_04["values"] = get_values(int(money - sum_01.get() - sum_02.get() - sum_03.get()))

    # Включаем возможность нажатия кнопки СТАРТ при выборе ставки
    if total > 0:
        start_button["state"] = "normal"
    else:
        start_button["state"] = "disabled"

    # Ставим отметку чекбокса в случае выбора ставки
    if sum_01.get() > 0:
        horse_01_game.set(True)
    else:
        horse_01_game.set(False)

    if sum_02.get() > 0:
        horse_02_game.set(True)
    else:
        horse_02_game.set(False)

    if sum_03.get() > 0:
        horse_03_game.set(True)
    else:
        horse_03_game.set(False)

    if sum_04.get() > 0:
        horse_04_game.set(True)
    else:
        horse_04_game.set(False)


def get_values(total):
    """Формирует список сумм для ставки"""
    # Создаем список
    value = []

    # Добавляем значения в список
    if total > 9:
        # Добавляем значения в список
        for i in range(10):
            value.append(i * int(total) // 10)
    # Если у пользователя меньше 10 денег, то предлагаем всего два варианта
    else:
        value.append(0)
        if total > 0:
            value.append(total)

    return value


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
        print("Ошибка сохранения, наш Ипподром закрывается!")
        quit(0)


def insert_text(s):
    """Добавляет строку в информационный чат"""
    text_diary.insert(INSERT, s + "\n")
    text_diary.see(END)


def horse_place_in_window():
    """Отрисовка изображения коней на игровом поле"""
    horse_01.place(x=int(x_01), y=20)
    horse_02.place(x=int(x_02), y=100)
    horse_03.place(x=int(x_03), y=180)
    horse_04.place(x=int(x_04), y=260)


def view_money():
    """Добавляет сообщение с указанием оставшейся суммы в информационный чат"""
    pass


# Создаём окно программы
root = Tk()

# Задаем значения высоты и ширины
WIDTH = 1024
HEIGHT = 600

# Позиции лошадей
x_01 = 20
x_02 = 20
x_03 = 20
x_04 = 20

# Клички лошадей
name_horse_01 = "Буцефал"
name_horse_02 = "Инцитат"
name_horse_03 = "Билли"
name_horse_04 = "Эклипс"

# Маркеры ситуаций
# Направление движения
reverse_01 = False
reverse_02 = False
reverse_03 = False
reverse_04 = False

# Движение
play_01 = True
play_02 = True
play_03 = True
play_04 = True

# Ускорение
fast_speed_01 = False
fast_speed_02 = False
fast_speed_03 = False
fast_speed_04 = False

# Переменные для денег
default_money = 10000  # Количество денег по умолчанию
money = 0  # Текущее количество денег
currency = "руб"  # Выбранная денежная единица

# Погода
weather = randint(1, 5)  # 1 - самая худшая, 5 - самая лучшая

# Время суток
time_day = randint(1, 4)  # 1 - ночь, 2 - утро, 3 - день, 4 - вечер

# Вычисляем координаты для размещения окна по центру
POS_X = root.winfo_screenwidth() // 2 - WIDTH // 2
POS_Y = root.winfo_screenheight() // 2 - HEIGHT // 2

# Установка заголовка
root.title("ИППОДРОМ")

# Запрещаем изменять размеры окна
root.resizable(False, False)

# Устанавливаем размеры и позицию окна
root.geometry(f"{WIDTH}x{HEIGHT}+{POS_X}+{POS_Y}")

# Устанавливаем фон
road_image = PhotoImage(file="road.png")
road = Label(root, image=road_image)
road.place(x=0, y=17)

# Устанавливаем изображение первой лошади
horse_01_image = PhotoImage(file="horse01.png")
horse_01 = Label(root, image=horse_01_image)

# Устанавливаем изображение второй лошади
horse_02_image = PhotoImage(file="horse02.png")
horse_02 = Label(root, image=horse_02_image)

# Устанавливаем изображение первой лошади
horse_03_image = PhotoImage(file="horse03.png")
horse_03 = Label(root, image=horse_03_image)

# Устанавливаем изображение первой лошади
horse_04_image = PhotoImage(file="horse04.png")
horse_04 = Label(root, image=horse_04_image)

# Отображаем лошадей
horse_place_in_window()

# Создаем и устанавливаем кнопку старта
start_button = Button(text="СТАРТ", font="arial 20", width=61, background="#37AA37")
start_button.place(x=20, y=370)
# Отключаем возможность нажатия кнопки СТАРТ
start_button["state"] = "disabled"

# Создаем текстовое поле для информационного чата
text_diary = Text(width=70, height=8, wrap=WORD)
text_diary.place(x=430, y=450)

# Создаем колесо прокрутки для информационного чата
scroll = Scrollbar(command=text_diary.yview(), width=20)
scroll.place(x=990, y=450, height=132)
text_diary["yscrollcommand"] = scroll.set

# Загружаем количество средств
money = load_money()

# Закрываем программу в случае, если у пользователя нет средств
if money <= 0:
    messagebox.showinfo("Стоп!", "На ипподром без средств заходить нельзя!")
    quit(0)

# Отображаем количество средств
label_all_money = Label(text=f"Осталось средств: {money} {currency}.", font="Arial 12")
label_all_money.place(x=20, y=565)

# Отображаем метки для ставок
label_horse_01 = Label(text="Ставка на лошадь №1")
label_horse_01.place(x=20, y=450)

label_horse_02 = Label(text="Ставка на лошадь №2")
label_horse_02.place(x=20, y=480)

label_horse_03 = Label(text="Ставка на лошадь №3")
label_horse_03.place(x=20, y=510)

label_horse_04 = Label(text="Ставка на лошадь №4")
label_horse_04.place(x=20, y=540)

# Отображаем чекбоксы для лошадей
horse_01_game = BooleanVar()
horse_01_game.set(0)
horse_check_01 = Checkbutton(text=name_horse_01, variable=horse_01_game, onvalue=1, offvalue=0)
horse_check_01.place(x=150, y=448)

horse_02_game = BooleanVar()
horse_02_game.set(0)
horse_check_02 = Checkbutton(text=name_horse_02, variable=horse_02_game, onvalue=1, offvalue=0)
horse_check_02.place(x=150, y=478)

horse_03_game = BooleanVar()
horse_03_game.set(0)
horse_check_03 = Checkbutton(text=name_horse_03, variable=horse_03_game, onvalue=1, offvalue=0)
horse_check_03.place(x=150, y=508)

horse_04_game = BooleanVar()
horse_04_game.set(0)
horse_check_04 = Checkbutton(text=name_horse_04, variable=horse_04_game, onvalue=1, offvalue=0)
horse_check_04.place(x=150, y=538)

# Запрещаем изменение чекбоксов
horse_check_01["state"] = "disabled"
horse_check_02["state"] = "disabled"
horse_check_03["state"] = "disabled"
horse_check_04["state"] = "disabled"

# Создаем выпадающие списки для ставок
bet_01 = ttk.Combobox(root)
bet_02 = ttk.Combobox(root)
bet_03 = ttk.Combobox(root)
bet_04 = ttk.Combobox(root)

# Отображаем выпадающие списки для ставко
bet_01["state"] = "readonly"
bet_01.place(x=280, y=450)

bet_02["state"] = "readonly"
bet_02.place(x=280, y=480)

bet_03["state"] = "readonly"
bet_03.place(x=280, y=510)

bet_04["state"] = "readonly"
bet_04.place(x=280, y=540)

# Создаем переменные для отображения суммы ставок
sum_01 = IntVar()
sum_02 = IntVar()
sum_03 = IntVar()
sum_04 = IntVar()

# Привязываем переменные
bet_01["textvariable"] = sum_01
bet_02["textvariable"] = sum_02
bet_03["textvariable"] = sum_03
bet_04["textvariable"] = sum_04

# Присваиваем функцию к выпадающему списку
bet_01.bind("<<ComboboxSelected>>", refresh_combo)
bet_02.bind("<<ComboboxSelected>>", refresh_combo)
bet_03.bind("<<ComboboxSelected>>", refresh_combo)
bet_04.bind("<<ComboboxSelected>>", refresh_combo)

# Обновляем значения выпадающих списков
refresh_combo("")

# Устанавливаем значения по умолчанию в выпадающих списка
bet_01.current(0)
bet_02.current(0)
bet_03.current(0)
bet_04.current(0)

# Запуск лошадей
start_button["command"] = run_horse

# Состояние лошадей (1 - лучше всех, 5 - хуже всех)
state_01 = randint(1, 5)
state_02 = randint(1, 5)
state_03 = randint(1, 5)
state_04 = randint(1, 5)


# Создаем коэффициенты выигрыша
win_coeff_01 = int(100 + randint(1, 30 + state_01 * 60)) / 100
win_coeff_02 = int(100 + randint(1, 30 + state_02 * 60)) / 100
win_coeff_03 = int(100 + randint(1, 30 + state_03 * 60)) / 100
win_coeff_04 = int(100 + randint(1, 30 + state_04 * 60)) / 100

# Отображаем погоду в информационном чате
view_weather()

# Отображаем информацию о лошадях
health_horse()

root.mainloop()
