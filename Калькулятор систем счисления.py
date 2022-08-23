def is_valid(system, num):
    for e in num:
        if e in "0123456789":
            if int(e) >= int(system):
                return False
        elif e != "A" and e != "B" and e != "C" and e != "D" and e != "E" and e != "F":
            return False
    return True


def is_valid_system(digit):
    while True:
        if digit.isdigit():
            if int(digit) <= 16:
                break
            else:
                digit = input("Введена неверная система счисления. Введите численное значение до 16:\n")
        else:
            digit = input("Введена неверная система счисления. Введите численное значение до 16:\n")
    return digit


def in_decimal():
    system = input("Введите систему счисления: (до 16 включительно)\n")
    is_valid_system(system)
    num, result = input("Введите число:\n"), 0
    while not is_valid(system, num):
        num = input("Введено неправильное число. Введите число выбранной системы счисления:\n")
    for i in range(len(num)):
        if num[i] == "A":
            result += int(10) * int(system) ** (len(num) - 1 - i)
        elif num[i] == "B":
            result += int(11) * int(system) ** (len(num) - 1 - i)
        elif num[i] == "C":
            result += int(12) * int(system) ** (len(num) - 1 - i)
        elif num[i] == "D":
            result += int(13) * int(system) ** (len(num) - 1 - i)
        elif num[i] == "E":
            result += int(14) * int(system) ** (len(num) - 1 - i)
        elif num[i] == "F":
            result += int(15) * int(system) ** (len(num) - 1 - i)
        else:
            result += int(num[i]) * int(system) ** (len(num) - 1 - i)
    return result


def from_decimal():
    system = input("Введите систему счисления: (до 16 включительно)\n")
    is_valid_system(system)
    num, result = input("Введите число:\n"), 0
    while not num.isdigit():
        num = input("Введено неправильное число. Введите число десятичной системы счисления:\n")
    result, remainder = [], 0
    num, system = int(num), int(system)
    while num > 1:
        remainder = num % system
        if remainder == 10:
            remainder = "A"
        elif remainder == 11:
            remainder = "B"
        elif remainder == 12:
            remainder = "C"
        elif remainder == 13:
            remainder = "D"
        elif remainder == 14:
            remainder = "E"
        elif remainder == 15:
            remainder = "F"
        num //= system
        result.append(remainder)
    if num == 1:
        result.append(num)
    return result[::-1]


init = input("В десятичную или из десятичной? (в/из)\n")
while init.lower() != "в" and init.lower() != "из":
    init = input("Неверый параметр. В десятичную или из десятичной? (в/из)\n")
if init.lower() == "в":
    print(in_decimal())
elif init.lower() == "из":
    print(*from_decimal(), sep="")
