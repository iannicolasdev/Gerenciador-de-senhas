import random 

caracteres = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'

print(''.join(random.choices(caracteres, k=12)))
