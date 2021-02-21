def addToInventory(invertory, items_list):
    for item in set(items_list):
        invertory.setdefault(item, 0)
        invertory[item] += items_list.count(item)

    return invertory


def displayInventory(inventory):
    print("Inventory:")
    total = 0

    for key, value in inventory.items():
        total += value
        print(f'{value} {key}')

    print(f"Total number of items: {total}")


inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

inv = addToInventory(inv, dragonLoot)
displayInventory(inv)
