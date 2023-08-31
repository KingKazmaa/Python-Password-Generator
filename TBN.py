# Password Generator
import random
# import math

print('Password Generator')

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@$%&*().,'

number = (input('Number of Passwords?'))
number = int(number)

length = input('Character Length?')
length = int(length)

print("WAAPAAAA!")
for pwd in range(number):
    passwords = ''
    for c in range(length):
        passwords += random.choice(chars)
print(passwords)