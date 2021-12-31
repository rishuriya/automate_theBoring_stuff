import random
streak=0
coin=0
t1=2
for experiment in range(10000):
    for toss in range(100):
        t=t1
        t1=random.randint(0,1)
        #print(t1,end=" ")
        #print(t)
        if(t==t1):
            
            coin=coin+1
            if(coin==6):
                streak=streak+1
                coin=0
        else:
            coin=0
probability=streak/100
print(streak)
print(probability)