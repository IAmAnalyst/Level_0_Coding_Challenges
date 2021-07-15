def commonCharacters(a,b):
    a=a.lower()
    b=b.lower()
    common=" "
    s=''
    for i in a:
        for l in range(len(b)):
            if((i==b[l]) & ~(i in common)):
                common+=i+','  
    for k in range(len(common)-1): 
        s+=common[k]

    return "The common characters/letters:"+s+'.'

print(commonCharacters("Philanie","Philasande"))