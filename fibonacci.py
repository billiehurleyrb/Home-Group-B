import numpy as np
def fib(n):
    Phi =((np.sqrt(5)+1)/2)
    phi = Phi-1
    fib_n = int(((Phi**n) - (-phi)**n)/np.sqrt(5))
    return fib_n

n = int(input('n = '))
suffixes = ['st','nd','rd','th']

if str(n)[-1] == '1':
    suffix = suffixes[0]
elif str(n)[-1] == '2':
    suffix = suffixes[1]
elif str(n)[-1] == '3':
    suffix = suffixes[2]
else:
    suffix = suffixes[3]

print(f'The {n}{suffix} Fibonacci number is {fib(n)}')
print('Billie')
<<<<<<< HEAD
print('Maya')
=======
print('Iva')
>>>>>>> 49d068db6df8546cf371ff40d2c59a03c706f5ba
