import random


def get_word():
    word_list = ["Ладонь", "Пылесос", "Король", "Полдник", "Зеркало", "Табурет", "Красота", "Волк",
                 "Переход", "Аквапарк", "Желание", "Конфета", "Учитель", "Опушка", "Песок", "Снежинка",
                 "Силач", "Корабль", "Куртка", "Сказка", "Пирог", "Звезда", "Сахар", "Пряник", "Лимон",
                 "Берег", "Горка", "Пирамида", "Дружба", "Рыба", "Телевизор", "Покрывало", "Секрет",
                 "Тесто", "Лужа", "Музыка", "Невидимка", "Трещина", "Кладовка", "Мультик", "Экран",
                 "Магазин", "Занавеска", "Свинья", "Дедушка", "Камень", "Свисток", "Молния", "Игрушка",
                 "Доброта", "Картошка", "Строитель", "Раковина", "Краб", "Дерево", "Стекло", "Подушка",
                 "Минута", "Замок", "Разговор", "Правда", "Прогулка", "Бульдозер", "Подоконник", "Сердце",
                 "Балкон", "Сосулька", "Кошка", "Картинка", "Штаны", "Прихожая", "Вечер", "Стакан", "Яма",
                 "Водопад", "Ветер", "Колесо", "Ложка", "Железо", "Палка", "Картон", "Пластилин", "Масло",
                 "Скатерть", "Грибок", "Книга", "Батон", "Корова", "Земля", "Остров", "Загадка", "Машина",
                 "Волна", "Голова", "Зарядка", "Птица", "Пятно", "Ведро", "Дождь", "Шапка"]
    return random.choice(word_list)


def display_hangman(tries):
    stages = ['''
--------
|      |
|      0
|     \\|/
|      |
|     / \\
-
              ''',
              '''
--------
|      |
|      0
|     \\|/
|      |
|     /
-
              ''',
              '''
--------
|      |
|      0
|     \\|/
|      |
|
-
              ''',
              '''
--------
|      |
|      0
|     \\|
|      |
|
-
              ''',
              '''
--------
|      |
|      0
|      |
|      |
|
-
              ''',
              '''
--------
|      |
|      0
|
|
|
-
              ''',
              '''
--------
|      |
|
|
|
|
-
              ''']
    return stages[tries]


def play(word):
    word = [e for e in word]
    word_completion = ["_"] * len(word)
    guessed_letters = []
    guessed_word = []
    tries = 6
    print("Давайте играть в угадайку слов!")
    while tries != 0:
        guessed = False
        print(display_hangman(tries))
        print(*word_completion)
        in_try = input("Введите букву или слово(русского алфавита):\n")
        in_try = in_try.upper()
        while True:
            for e in in_try:
                if e not in "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ":
                    in_try = input("Неправильно. Введите букву русского алфавита:\n")
                    in_try = in_try.upper()
                else:
                    guessed = True
            if guessed:
                break
        while in_try in guessed_letters:
            in_try = input("Такая буква уже была. Попробуйте другую:\n")
            in_try = in_try.upper()
        while in_try in guessed_word:
            in_try = input("Такое слово уже было. Попробуйте другое:\n")
            in_try = in_try.upper()
        while not in_try:
            in_try = input("Вы ничего не ввели. Попробуйте ещё раз:\n")
            in_try = in_try.upper()
        if len(in_try) == 1:
            if in_try in word:
                for i in range(len(word)):
                    if word[i] == in_try:
                        word_completion[i] = in_try
                guessed_letters.append(in_try)
                if "_" not in word_completion:
                    print("Поздравляем, вы угадали слово! Вы победили!")
                    break
            else:
                print("К сожалению, такой буквы нет!")
                tries -= 1
                guessed_letters.append(in_try)
        else:
            in_try = [e for e in in_try]
            if len(in_try) != len(word):
                print("Длина вашего слова не равна длине загаданного.")
                continue
            if in_try == word:
                print("Поздравляем, вы угадали слово! Вы победили!")
                break
            else:
                print("К сожалению, неправильно.")
                guessed_word.append(in_try)
                tries -= 1
    if tries == 0:
        print("Вы проиграли.")
    print(display_hangman(tries))
    print(*word)


play(get_word().upper())
