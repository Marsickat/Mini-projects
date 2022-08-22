import random


def generate_password(lenght, chars):
    password = ""
    for i in range(lenght):
        password += random.choice(chars)
    return password


def is_valid(value):
    return value.isdigit()


digits = "0123456789"
lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
punctuation = "!#$%&*+-=?@^_"

chars = ""

quantity = input("Количество паролей для генерации?\n")
if not is_valid(quantity):
    quantity = input("Пожалуйста, введите число:\n")
lenght = input("Длина одного пароля?\n")
if not is_valid(lenght):
    lenght = input("Пожалуйста, введите число:\n")
quantity, lenght = int(quantity), int(lenght)
digits_in = input(f"Включать ли цифры {digits} (да/нет)\n")
uppercase_letters_in = input(f"Включать ли прописные буквы {uppercase_letters} (да/нет)\n")
lowercase_letters_in = input(f"Включать ли строчные буквы {lowercase_letters} (да/нет)\n")
punctuation_in = input(f"Включать ли символы {punctuation} (да/нет)\n")
exception = input("Исключать ли неоднозначные символы il1Lo0O (да/нет)\n")

if digits_in.lower() == "да":
    chars += digits
if uppercase_letters_in.lower() == "да":
    chars += uppercase_letters
if lowercase_letters_in.lower() == "да":
    chars += lowercase_letters
if punctuation_in.lower() == "да":
    chars += punctuation
if exception.lower() == "да":
    for c in "il1Lo0O":
        chars = chars.replace(c, "")

for i in range(quantity):
    print(generate_password(lenght, chars))
