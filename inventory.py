# Revisit this.


def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in sorted(inventory.items()):
        if k != "dagger":
            print(str(v) + " " + k)
    for k, v in inventory.items():
        if k == "dagger":
            print(str(v) + " " + k)
        item_total += v
    print("Total number of items: " + str(item_total))


stuff = {"rope": 1, "torch": 6, "gold coin": 42, "dagger": 1, "arrow": 12}

displayInventory(stuff)
