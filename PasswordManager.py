import json
from Functions import *

def add_details(site, user, passw):
    try:
        with open("details.json", "r") as f:
            passwords = json.load(f)
    except FileNotFoundError:
        passwords = {}
    username = ''.join(format(b, '08b') for b in user.encode())
    password = ''.join(format(b, '08b') for b in passw.encode())
    list = [encrypt(int(username)), encrypt(int(password))]
    passwords[site] = list

    with open("details.json", "w") as f:
        json.dump(passwords, f)

    print('Details added')

def delete_details(site):
    passwords[site] = ''
    print('Details deleted')

def view_details(site):
    details = passwords[site]
    list = [decrypt(details[0]), decrypt(details[1])]
    return list


while True:
    inp = input("Options: add, delete, view, exit: ")
    if  inp == 'add':
        site = input('Enter site: ')
        username = input('Enter username: ')
        password = input('Enter password: ')
        add_details(site, username, password)
    elif inp == 'delete':
        site = input('Enter site: ')
        delete_details(site)
    elif inp == 'view':
        site = input('Enter site: ')
        list = view_details(site)
        print(list)
    elif inp == 'exit':
        break
