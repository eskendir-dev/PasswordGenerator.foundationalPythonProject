import random

symbols = 'abcdefghijklmnopqrstuvwxzABCDEFGHIJKLMNOPQRSTUVWXZ1234567890~`!@#$%^&*()_-+={[}]|\:;"?'
password = ''
length = int(input('Write length of password: \n')) 

for i in range(length): 
    random_symbol = random.choice(symbols)
    password += random_symbol
        
print('Here is your password: ', password)