def Convert_to_hours_and_Minutes(n):
    hours=n//60
    minutes=n%60
    if (hours<2) & (minutes>1):
        return f'{hours} hour,{minutes} minutes.'
    if (hours>=2) & (minutes>1):   
        return f'{hours} hours, {minutes} minutes.' 
    else:
        return f'{hours} hours, {minutes} minute.'     
print(Convert_to_hours_and_Minutes(71))