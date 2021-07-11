import math
def Maximum(*args):
    max=-math.inf    #n case we have to include negative numbers
    for i in args:
        for l in range(len(args)):
            if max<i:
              if i>=args[l]:
                max=i
              else:
                max=args[l]    
    return "The maximum number is:" , max
    #if (a>=b) & (a>=c):
      #  return a
    #elif (b>=a) & (b>=c):
    #    return b
    #else:
    #    return c
print(Maximum(-6,-54,-3,-2,-1,0,2,78,100))          