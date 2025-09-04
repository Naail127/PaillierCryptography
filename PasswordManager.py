import json
from Functions import *
from key import my_dictionary, revered_dic

def add_details(site, user, passw):
    var = ""
    var2 = ''
    try:
        with open("details.json", "r") as f:
            passwords = json.load(f)
    except FileNotFoundError:
        passwords = {}
    for char in user:
        var = var + my_dictionary[char]
    for char in passw:
        var2 = var2 + my_dictionary[char]
    list = [encrypt(int(var)), encrypt(int(var2))]
    passwords[site] = list

    with open("details.json", "w") as f:
        json.dump(passwords, f)

    print('Details added')

def delete_details(site):
    try:
        with open("details.json", "r") as f:
            passwords = json.load(f)
    except FileNotFoundError:
        print(site + "not found")
    passwords[site] = ''
    with open("details.json", "w") as f:
        json.dump(passwords, f)
    print('Details deleted')

def view_details(site):
    try:
        with open("details.json", "r") as f:
            passwords = json.load(f)
    except FileNotFoundError:
        print(site + "not found")
    details = passwords.get(site,0)
    var1 = ''
    var2 = ''
    temp = ''
    value = 0
    if details == 0:
        print('Details not found')
        return -1

    username = str(decrypt(details[0]))
    password = str(decrypt(details[1]))
    if len(username) % 2 :
        username = "0" + username
    if len(password) % 2 :
        password = "0" + password
    for char in username:
        value = value + 1
        if value % 2 == 0:
            temp = temp + char
            temp = revered_dic[temp]
            var1 = var1 + temp
        else:
            temp = char
    username = var1
    for char in password:
        value = value + 1
        if value % 2 == 0:
            temp = temp + char
            temp = revered_dic[temp]
            var2 = var2 + temp
        else:
            temp = char
    password = var2

    return username, password


#while True:
#    inp = input("Options: add, delete, view, exit: ")
#    if  inp == 'add':
#        site = input('Enter site: ')
#        username = input('Enter username: ')
#        password = input('Enter password: ')
#        add_details(site, username, password)
#    elif inp == 'delete':
#        site = input('Enter site: ')
#        delete_details(site)
#    elif inp == 'view':
#        site = input('Enter site: ')
#        x,y = view_details(site)
#        print(" Username: ",x,"\n","Password: ",y)
#    elif inp == 'exit':
#        break
