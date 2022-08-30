import random

result_lst = []

for experimental_number in range(10000):
    number_of_streaks = 0
    lst = []
    pause = 0
    for i in range(100):
        num = random.randint(0, 1)
        lst.append(num)

    for j in range(len(lst) - 6):
        if pause == 0:
            if lst[j:j + 6] == [0, 0, 0, 0, 0, 0]:
                number_of_streaks += 1
                pause = 6
            elif lst[j:j + 6] == [1, 1, 1, 1, 1, 1]:
                number_of_streaks += 1
                pause = 6
        else:
            pause -= 1

    result = number_of_streaks / 100
    result_lst.append(result)

probability = 0

for e in result_lst:
    probability += e

print(f"Вероятность появления серии из шести повторяющихся элементов: {probability / 10000}")
