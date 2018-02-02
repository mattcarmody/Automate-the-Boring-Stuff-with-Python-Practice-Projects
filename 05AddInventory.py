# Function copied from previous project.
def display_inventory(inventory):
    total = 0
    print('Inventory:')
    for k, v in inventory.items():
        print('{} {}'.format(v, k))
        total += v
    print('Total number of items: {}'.format(total))

# Challenge function, needs to work with duplicates.
def add_inventory(inventory, newItems):
    for i in range(len(newItems)):
        if newItems[i] in inventory.keys():
            inventory[newItems[i]] += 1
        else:
            inventory.setdefault(newItems[i], 1)
    return inventory

heroInv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

print("\nWhen he arrives, the hero has a few things.")
display_inventory(heroInv)
print("\nThen he slayed the dragon! Now he has a few more things.")
display_inventory(add_inventory(heroInv, dragonLoot))
