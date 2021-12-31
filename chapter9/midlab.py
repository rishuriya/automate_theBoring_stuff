file=open("input.txt","r")
line=file.read().split()
word=input("Enter an adjective:\n")
new_line=''
for i in range(len(line)):
    if line[i]=='ADJECTIVE':
        line[i]=word
        break
i=0
word=input("Enter an noun:\n")
for j in range(len(line)):
    if line[j]=='NOUN':
        line[j]=word
        break
word=input("Enter an verb:\n")
for i in range(len(line)):
    if line[i]=='VERB.':
        line[i]=word+"."
        break
word=input("Enter an noun:\n")
for j in range(len(line)):
    if line[j]=='NOUN':
        line[j]=word
        break
for t in range(len(line)):
    new_line=new_line+line[t]+" "
    print(line[t],end=" ")
fileout=open("output.txt",'w')
fileout.write(new_line)