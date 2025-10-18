from functools import lru_cache

# task 2
# создать **рекурсивную** функцию fibonacci, которая принимает целое число N
# и возвращает N-ное число в последовательности Фибоначчи
# важно - у вас при больших числах (больше 20 и далее) - программа будет тупить
# пока что это норма


MY_CACHE: int = {}

def fib(n):
    if n in MY_CACHE:
        return MY_CACHE[n]
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        ggg = fib(n-1) + fib(n-2)
        MY_CACHE[n] = ggg 
        return ggg
        

g = ""
for i in range(21):
    g += str(fib(i)) + ' '
    
print(g)
