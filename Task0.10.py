def commonCharacters(a,b):
    a=a.lower()
    b=b.lower()
    common=" "
    for i in a:
        for l in range(len(b)):
            if((i==b[l]) & ~(i in common)):
                common+=i+","
    return "The common characters/letters:"+common

print(commonCharacters("Philanie","Philasande"))