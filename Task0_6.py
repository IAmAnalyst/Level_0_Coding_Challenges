def Maximum(*args):  #*args allows function to accept any number of arguments     
    max=-9999999999   #n case we have to include negative numbers
    for i in args:
        for l in range(len(args)):
            if max<i:
              if i>=args[l]:
                max=i
              else:
                max=args[l]    
    return f"The maximum number is: {max}"
print(Maximum(-6,-54,-3,-2,-1,0,2,78,100))          