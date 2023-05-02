def result(some):
    for i in range(len(some)):
        if some[i] != some[-2]:
            print(some[i], end=", ")
        else:
            print(f"{some[i]} и {some[i + 1]}")
            break


lst = []
while True:
    text = input("Введите текст (для окончания введите пустую строку):\n")
    while not lst:
        if not text:
            text = input("Вы ничего не ввели! Введите текст:\n")
        else:
            break
    if not text:
        while len(lst) == 1:
            text = input("Вы ввели одно значение! Введите текст:\n")
            while not text:
                text = input("Вы ничего не ввели! Введите текст:\n")
            else:
                break
    if not text:
        break
    lst.append(text)
result(lst)
