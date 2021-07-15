def Vowels_in_this_string(s):
    s=s.lower()
    v="aeiou"
    vowels=''
    c=''
    for i in s:
        for l in range(len(v)):
            if((i==v[l]) & ~(i in vowels )):
                vowels+=i+','
    for k in range(len(vowels)-1):
        c+=vowels[k]
    
    return "Vowels : "+c+' .'   

print(Vowels_in_this_string("umuzi"))