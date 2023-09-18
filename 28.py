def sum(a,b):
    res=a+b
    if a==res or b==res:
        return a
    return sum(a+1,b-1)

a=int(input("Введите первое число: "))
b=int(input("Введите второе число: "))
print(sum(a,b))