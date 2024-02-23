def calc(list):
    if len(list)==0:
        return 0
    else:
        return list[0]**2 + calc(list[1:]) 

list = [1, 3, 4, 2, 5]
x = calc(list)        
print(x)

def fib(x):
    if x == 0 or x == 1:
        return 1
    else:
        return fib(x-1) + fib(x-2)
print(fib(4))

a = {1, 2, 3}
b = {0, 3, 4, 5}
print(a & b)