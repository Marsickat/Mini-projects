import random


def is_valid(value, right):
    return value.isdigit() and 1 <= int(value) <= int(right)


right = input("Введите целое число, от 1 до которого оно будет загадано:\n")
while not right.isdigit():
    right = input("А может быть всё-таки введём целое число:\n")
right = int(right)
print(f"Введите число от 1 до {right}:")
num = random.randint(1, right)
attempts = 0
while True:
    digit = input()
    if is_valid(digit, right):
        digit = int(digit)
        if digit < num:
            print("Ваше число меньше загаданного, попробуйте еще разок")
            attempts += 1
        elif digit > num:
            print("Ваше число больше загаданного, попробуйте еще разок")
            attempts += 1
        elif digit == num:
            attempts += 1
            print(f"Вы угадали, поздравляем! Количество затраченных попыток: {attempts}")
            again = input("Напишите \"да\", если хотите сыграть ещё раз:\n")
            if again.lower() == "да":
                print("\nНачинаем новую игру!")
                right = input("Введите целое число, от 1 до которого оно будет загадано:\n")
                while not right.isdigit():
                    right = input("А может быть всё-таки введём целое число:\n")
                right = int(right)
                print(f"Введите число от 1 до {right}:")
                num = random.randint(1, right)
                attempts = 0
                continue
            else:
                break
    else:
        print(f"А может быть всё-таки введём целое число от 1 до {right}?")


print("Добро пожаловать в числовую угадайку!\n")

print("Спасибо, что играли в числовую угадайку. Ещё увидимся...")
