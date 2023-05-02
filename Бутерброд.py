import pyinputplus as pyip

bread = pyip.inputMenu(["Цельнозерновой", "Белый", "Ржаной"], prompt="Выберите хлеб:\n", numbered=True)
meat = pyip.inputMenu(["Курица", "Индейка", "Ветчина", "Тофу"], prompt="Выберите мясо:\n",numbered=True)
cheese_on = pyip.inputYesNo("Добавить сыр?\n", yesVal="да", noVal="нет")
if cheese_on == "да":
    cheese = pyip.inputMenu(["Чеддер", "Швейцарский", "Моцарелла"], prompt="Выберите сыр:\n", numbered=True)
total = pyip.inputInt("Сколько бутербродов вы хотите?\n", greaterThan=1)

cost = 0
if bread == "Цельнозерновой":
    cost += 9
elif bread == "Белый":
    cost += 7
else:
    cost += 11

if meat == "Курица":
    cost += 38
elif meat == "Индейка":
    cost += 28
elif meat == "Ветчина":
    cost += 17
else:
    cost += 28

if cheese_on == "да":
    if cheese == "Чеддер":
        cost += 19
    elif cheese == "Швейцарский":
        cost += 15
    else:
        cost += 18

print(f"Сумма вашего заказа - {cost * total} руб.")
