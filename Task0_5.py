def Area_of_Triangle(a,b,c): #using Heron's formula
    s=(a+b+c)/2
    A=(s*(s-a)*(s-b)*(s-c))**0.5
    return A

print(f"The area of this triangle is: {Area_of_Triangle(4,13,15)}")