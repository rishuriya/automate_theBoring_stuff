import pyinputplus as pyip
rate=0
cheese=0
mayo=0
bread=pyip.inputMenu(choices=['White', 'Brown', 'Sourdough'])
if bread=='White':
    bread=20
    rate=rate+bread
elif bread=='Brown':
    bread=25
    rate=rate+bread
elif bread=='Sourdough':
    bread=30
    rate=rate+bread
#print(rate)
protein=pyip.inputMenu(['Chicken','Turkey','Ham','Tofu'])
if protein=='Chicken':
    protein=30
    rate=rate+protein
elif protein=='Turkey':
    protein=30
    rate=rate+protein
elif protein=='Ham':
    protein=25
    rate=rate+protein
elif protein=='Tofu':
    protein= 35
    rate=rate+protein
#print(rate)
chee=pyip.inputYesNo(prompt="Do You Want Cheese (Yes/No): ")
if chee=='yes':
    cheese=pyip.inputMenu(['Cheddar','Swiss','Mozzarella'])
    if cheese=='Cheddar':
        cheese=20
        rate=rate+cheese
    elif cheese=='Swiss':
        cheese=30
        rate=rate+cheese
    elif cheese=='Mozzarella':
        cheese=40
        rate=rate+cheese
#print(rate)
mayo=pyip.inputYesNo(prompt="Do You Want mayo, mustard, lettuce, or tomato (Yes/No): ")
if mayo=='yes':
    mayo=10
    rate=rate+mayo
else:
    mayo=0
quantity=pyip.inputInt(prompt="How Many Sandwiches you Want: ",greaterThan=0)
rate=rate*quantity
print("Cost Of bread   {}".format(bread))
print("Cost of protein {}".format(protein))
if chee=="yes":
    print("Cost of Cheese  {}".format(cheese))
if mayo!="no":
    print("Cost of Stuff   {}".format(mayo))
print("Total Quantity  {}".format(quantity))
print("Total Cost      ",end="")
print(rate)

