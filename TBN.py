# Password Generator
import random

# I was trying to clean it up but for some reason I cant access the name variable from the second function. Any help is appreciated!

CHARS = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@$%&*().,'

def prompt_user():
    while True:
        print('Want a Password?')
        length = input('Character Length? ')
        if length.isdigit():
            length = int(length)
            break
        else:
            print('must be a number...')
            print(f"{length}")
    return length


def get_password():
    for pwd in range(length):
        passwords += random.choice(CHARS)
        print("WAAPAAAA!")
    print(passwords)
    
    
def main():
    prompt_user()
    get_password()

main()