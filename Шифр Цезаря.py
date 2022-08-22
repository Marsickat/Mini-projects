def is_valid(language, text):
    eng_alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwzyz"
    rus_alpha = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    if language.lower() == "английский":
        for c in text:
            if str(c).isalpha() and c not in eng_alpha:
                return False
    elif language.lower() == "русский":
        for c in text:
            if str(c).isalpha() and c not in rus_alpha:
                return False
    return True


def caesar(direction, language, step, text):
    result = ""
    upper_eng_alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lower_eng_aplha = "abcdefghijklmnopqrstuvwzyz"
    upper_rus_alpha = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    lower_rus_alpha = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    if language.lower() == "английский":
        alpha = 26
        upper_alpha = upper_eng_alpha
        lower_alpha = lower_eng_aplha
    else:
        alpha = 33
        upper_alpha = upper_rus_alpha
        lower_alpha = lower_rus_alpha
    for i in range(len(text)):
        if str(text[i]).isalpha():
            if direction.lower() == "вправо":
                if text[i].isupper():
                    elem = upper_alpha.index(text[i])
                    result += upper_alpha[(elem + step) % alpha]
                elif text[i].islower():
                    elem = lower_alpha.index(text[i])
                    result += lower_alpha[(elem + step) % alpha]
            else:
                if text[i].isupper():
                    elem = upper_alpha.index(text[i])
                    result += upper_alpha[(elem - step) % alpha]
                elif text[i].islower():
                    elem = lower_alpha.index(text[i])
                    result += lower_alpha[(elem - step) % alpha]
        else:
            result += text[i]
    return result


direction = input("В какую сторону производить сдвиг? (влево/вправо)\n")
while direction.lower() != "влево" and direction.lower() != "вправо":
    direction = input("Введено неверное направление.\nВ какую сторону производить сдвиг? (влево/вправо)\n")
language = input("Какой язык переводить? (английский/русский)\n")
while language.lower() != "английский" and language.lower() != "русский":
    language = input("Введен неверный язык.\nКакой язык переводить? (английский/русский)\n")
step = input("Какой шаг сдвига? (численное значение)\n")
while not step.isdigit():
    step = input("Введено неверное значение. Какой шаг сдвига? (численное значение)\n")
step = int(step)

text = input("Введите текст:\n")
if language.lower() == "русский":
    while not is_valid(language, text):
        text = input("Обнаружены буквы не русского алфавита. Введите русский текст:\n")
elif language.lower() == "английский":
    while not is_valid(language, text):
        text = input("Обнаружены буквы не английского алфавита. Введите английский текст:\n")

print(caesar(direction, language, step, text))
