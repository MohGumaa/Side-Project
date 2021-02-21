stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def displayInventory(inventory):
    print("Inventory:")
    total = 0

    for key, value in inventory.items():
        total += value
        print(f'{value} {key}')

    print(f"Total number of items: {total}")

displayInventory(stuff)
