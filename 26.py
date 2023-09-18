def rec(a,b):
    
    if b==1:
        return a
    return(a*rec(a,b-1))
    
a=int(input("введите число "))
b=int(input("введите степень "))
print(rec(a,b))