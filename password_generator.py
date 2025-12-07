import random

symbols = 'abcdefghijklmnopqrstuvwxzABCDEFGHIJKLMNOPQRSTUVWXZ1234567890~`!@#$%^&*()_-+={[}]|\:;"?'
password = ''

while True:
    try:
        length = int(input('Write length of password: \n')) 
        break
    except ValueError:
        print("Error: Please enter a valid whole number. Try again.")

for i in range(length): 
    random_symbol = random.choice(symbols)
    password += random_symbol
    
print('Here is your password: ', password)
