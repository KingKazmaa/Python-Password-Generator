# Password Generator
import random

CHARS = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@$%&*().,'
global length

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