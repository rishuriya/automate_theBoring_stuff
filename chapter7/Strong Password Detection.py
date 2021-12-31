def strongPwd(data):
    #i=len(data)
    upper=0
    lower=0
    num=0
    for i in range(len(data)):
        if data[i]>='A' and data[i]<='Z':
            upper=upper+1
        if data[i]>='a' and data[i]<='z':
            lower=lower+1
        if data[i]>='1' and data[i]<='9':
            num=num+1
    if upper>0 and lower>0 and num>0 and len(data)>=8:
        return "Strong"
    else:
        return "Weak"
i = input()
result=strongPwd(i)
print(result)