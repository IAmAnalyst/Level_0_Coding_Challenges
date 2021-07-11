def Convert_to_hours_and_Minutes(n):
    hours=n//60
    minutes=n%60
    return hours, " hours and", minutes, "minute(s)"  
print(Convert_to_hours_and_Minutes(120))