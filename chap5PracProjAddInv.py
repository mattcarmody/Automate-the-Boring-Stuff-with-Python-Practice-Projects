#!python3
# chap5PracProjAddInv.py - Update inventory of a character.

# Display Inventory function, copied from previous project.
def displayInventory(inventory):
    total = 0
    print('Inventory:')
    for k, v in inventory.items():
        print(str(v) + ' ' + str(k))
        total += v
    print('Total number of items: ' + str(total))

# Add to Inventory function, needs to work with duplicates.
def addToInventory(inventory, addedItems):
    for i in range(len(addedItems)):
        if addedItems[i] in inventory.keys():
            inventory[addedItems[i]] += 1
        else:
            inventory.setdefault(addedItems[i], 1)
    return inventory

inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)
