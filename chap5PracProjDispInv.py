#!python3
# chap5PracProjDispInv.py - Display a character's inventory.

stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def displayInventory(inventory):
    total = 0
    print('Inventory:')
    for k, v in inventory.items():
        print(str(v) + ' ' + str(k))
        total += v
    print('Total number of items: ' + str(total))

displayInventory(stuff)
