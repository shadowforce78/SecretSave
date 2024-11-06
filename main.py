import cryptography
import os

file = 'data.json'

def first_start(file):
    if not os.path.exists(file):
        password = input('Enter password: ')
        create_file(file, password)
    else:
        password = input('Enter password: ')
        # Check if password is correct
        with open(file, 'r') as f:
            data = f.read()
            if password == data['password']:
                print('Correct password')
            else:
                print('Incorrect password')
                exit()
    return password


def create_file(file, password):
    # Create data.json and add password as a parent element for other data to be stored
    with open(file, 'w') as f:
        f.write('{"password": "' + password + '"}')
def main():
    password = first_start(file)
    print(password)
    
main()