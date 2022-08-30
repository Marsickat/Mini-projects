def collatz(number):
    if number % 2 == 0:
        return number // 2
    elif number % 2 == 1:
        return 3 * number + 1


number = int(input("Введите число: "))
print(number)
while number != 1:
    number = collatz(number)
    print(number)
