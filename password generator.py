# Password Generator
import random

print('Want a Password?')

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@$%&*().,'

number = (input('Press a number and hit Enter: '))
number = int(number)

length = input('Character Length? ')
length = int(length)

print("WAAPAAAA! Your password is:")
for pwd in range(number):
    passwords = ''
    for c in range(length):
        passwords += random.choice(chars)
print(passwords)