def display_inventory(inventory):
    print("Инвентарь:")
    item_total = 0
    for k, v, in inventory.items():
        print(f"    {k} - {v}")
        item_total += v
    print(f"Всего элементов: {item_total}")


def add_to_inventory(inventory, added_items):
    for e in added_items:
        if e in inventory:
            inventory[e] += 1
        else:
            inventory[e] = 1
    return inventory


inv = {"золотая монета": 42, "верёвка": 1}
dragon_loot = ["золотая монета", "кинжал", "золотая монета", "золотая монета", "рубин"]
inv = add_to_inventory(inv, dragon_loot)
display_inventory(inv)
