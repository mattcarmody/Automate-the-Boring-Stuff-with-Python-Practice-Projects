INV = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def display_inventory(inventory):
    total = 0
    print('Inventory:')
    for k, v in inventory.items():
        print('{} {}'.format(v, k))
        total += v
    print('Total number of items: {}'.format(total))

display_inventory(INV)
