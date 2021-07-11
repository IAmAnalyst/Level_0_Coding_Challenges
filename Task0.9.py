def Vowels_in_this_string(s):
    s=s.lower()
    v="aeiou"
    vowels=" "

    for i in s:
        for l in range(len(v)):
            if((i==v[l]) & ~(i in vowels )):
                vowels+=i+","
    return "Vowels :"+ vowels    
print(Vowels_in_this_string("umuzi"))