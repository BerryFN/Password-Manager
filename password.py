#Password Manager: Store passwords and usernames for websites/apps
#Be able to view your passwords and users by asking

import os
import json

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

print("Password Manager")
Enter = input("Press enter to start:")

#Login/Create account

def load_accounts():
    if not os.path.exists("accounts.json"):
        return {}
    with open("accounts.json", "r") as f:
        return json.load(f)

def save_accounts(accounts):
    with open("accounts.json", "w") as f:
        json.dump(accounts, f)

#Saved Logins Def Goes Here

def load_passwords():
    if not os.path.exists("save_passwords.json"):
        return {}
    with open("save_passwords.json", "r") as f:
        return json.load(f)

def save_passwords(passwords):
    with open("save_passwords.json", "w") as f:
        json.dump(passwords, f, indent=4)

clear_screen()
print("(Create New Account/Login)")
print("1. New Account ")
print("2. Login")
print("3. Exit Program")
account = input("(1./2./3.): ")

if account == '3':
    print("Exiting...")

#Creating New Account
if account == '1':
    print("Create a login")
    accounts = load_accounts()
    name = input("Enter your Username: ")
    while name in accounts:
        print("Username already exists!")
        input("Press Enter to try again...")
        clear_screen()
        name = input("Enter your Username: ")
    passkey = input("Enter your Password: ") 
    accounts[name] = passkey
    save_accounts(accounts) 
    clear_screen()


    while True:
        print("Welcome back ", name, " to your password manager")
        print("Choose an option:")
        print("1. Store a Password")
        print("2. View Saved Passwords")
        print("3. Exit and Sign out")
        choice = input("(1./2./3.):  ")

        if choice == '1':
            clear_screen()
            print("Save a Password:")
            passwords = load_passwords()

            if name not in passwords:
                passwords[name] = []

            saved_name = input("Enter Website or Application Name:  ")
            username = input("Enter Email, Phone Number, or Username:  ")
            password = input("Enter Website or Applications Password:  ")

            passwords[name].append({
                "site": saved_name,
                "username": username,
                "password": password
            })

            save_passwords(passwords)
            print("Password Saved Successfully!")
            input("Press Enter to continue...")
            clear_screen()
            continue
        
        elif choice == '2':
            clear_screen()
            passwords = load_passwords()

            user_data = passwords.get(name, [])
            if user_data:
                print("Here are your save passwords!")
                sorted_data = sorted(user_data, key=lambda x: x['site'])

                clear_screen()
                for idx, entry in enumerate(sorted_data, 1):
                    print(f"{idx}. {entry['site']} - {entry['username']} - {entry['password']}")
                input("Press Enter To Continue...")
                clear_screen()
                continue
            else:
                clear_screen()
                print("No saved passwords...")
                input("Press Enter To Continue...")
                clear_screen()
                continue

        elif choice == '3':
            clear_screen()
            print("Signing Out....")
            break

#Login to Account
elif account == '2':
    accounts = load_accounts()
    name = input("Enter a Username: ")
    passkey = input("Enter a Password: ")
    while name not in accounts or accounts[name] != passkey:
        print("Invalid login.")
        input("Press Enter to try again...")
        clear_screen()
        name = input("Enter a Username: ")
        passkey = input("Enter a Password: ")

    clear_screen()
    while True:
        print("Welcome back ", name, " to your password manager")
        print("Choose an option:")
        print("1. Store a Password")
        print("2. View Saved Passwords")
        print("3. Exit and Sign out")
        choice = input("(1./2./3.):  ")

        if choice == '1':
            clear_screen()
            print("Save a Password:")
            passwords = load_passwords()

            if name not in passwords:
                passwords[name] = []

            saved_name = input("Enter Website or Application Name:  ")
            username = input("Enter Email, Phone Number, or Username:  ")
            password = input("Enter Website or Applications Password:  ")

            passwords[name].append({
                "site": saved_name,
                "username": username,
                "password": password
            })

            save_passwords(passwords)
            print("Password Saved Successfully!")
            input("Press Enter to continue...")
            clear_screen()
            continue
        
        elif choice == '2':
            clear_screen()
            passwords = load_passwords()

            user_data = passwords.get(name, [])
            if user_data:
                print("Here are your save passwords!")
                sorted_data = sorted(user_data, key=lambda x: x['site'])

                clear_screen()
                for idx, entry in enumerate(sorted_data, 1):
                    print(f"{idx}. {entry['site']} - {entry['username']} - {entry['password']}")
                input("Press Enter To Continue...")
                clear_screen()
                continue
            else:
                clear_screen()
                print("No saved passwords...")
                input("Press Enter To Continue...")
                clear_screen()
                continue

        elif choice == '3':
            clear_screen()
            print("Signing Out....")
            break
