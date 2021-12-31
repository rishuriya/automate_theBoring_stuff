d=input("Input in DD/MM/YYYY format: ").rstrip()
date=d.split("/")
day=int(date[0])
month=int(date[1])
year=int(date[2])
#print(month)
if day<32 and month!=4 and month!=6 and month!=9 and month!=11 and month!=2:
    #print("i")
    if month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12:
        print("valid")
    else:
        print("invalid")
elif day<31 and month!=2:
    #print("i1")
    if month==4 or month==6 or month==9 or month==11:
        print("valid")
    else:
        print("invalid")
elif month==2:
    #print("i2")
    if year%4==0 and day<30:
        print("Valid")
    elif day<29:
        print("Valid")
    