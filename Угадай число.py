import random


def is_valid(value):
    return value.isdigit() and 1 <= int(value) <= 100


num = random.randint(1, 100)
print("Добро пожаловать в числовую угадайку!\n\nВведите целое число от 1 до 100:")

while True:
    digit = input()
    if is_valid(digit):
        digit = int(digit)
        if digit < num:
            print("Ваше число меньше загаданного, попробуйте еще разок")
        elif digit > num:
            print("Ваше число больше загаданного, попробуйте еще разок")
        elif digit == num:
            print(f"Вы угадали, поздравляем!")
            break
    else:
        print("А может быть всё-таки введём целое число от 1 до 100?")

print("Спасибо, что играли в числовую угадайку. Ещё увидимся...")
