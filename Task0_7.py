def Celsius_to_Fahrenheit(c):
    F=((c/5)*9)+32

    return f'This temperature is {F} degrees fahrenheit'


def Fahrenheit_to_Celcius(f):
    C=((f-32)*5)/9

    return f'This temperature is {C} degrees celsius'


print(Fahrenheit_to_Celcius(98.6))