def addToInventory(inventory, addedItems):
    key=list(inventory.keys())
    for i in range(len(addedItems)):
        t=0
        for j in range(len(key)):
           if key[j]==addedItems[i]:
               t=t+1
        if t==0:
            inventory.update({addedItems[i]:1})
            key.append(addedItems[i])
        else:
            inventory[addedItems[i]]=inventory[addedItems[i]]+t
    return inventory
inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        print(v, k)
        item_total=v+item_total
    print("Total number of items: " + str(item_total))
displayInventory(inv)