def printTable(data):
    ind=[]
    final=[]
    for i in range(len(data)):
        a=0
        t=len(data[i])
        for j in range(t):
            a1=len(data[i][j])
            if a1>a:
                a=a1
        ind.append(a)
    i=0
    print(ind)
    j=0
    for i in range(len(data[i])):
        for j in range(len(data)):
            b=ind[j]-len(data[j][i])
            for z in range(b):
                print(" ",end="")
            x=data[j][i]
            print(x,end=" ")
        print()
tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]
result=printTable(tableData)