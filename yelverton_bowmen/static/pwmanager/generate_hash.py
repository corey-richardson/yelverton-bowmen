from werkzeug.security import generate_password_hash, check_password_hash
from pwinput import pwinput
import os, sys

def prompts():
    matching = False
    while not matching:
        username = input("Username: ")
        password = pwinput(prompt='Password: ')
        repeat_password = pwinput(prompt='Repeat Password: ')
        
        if password == repeat_password:
            matching = True
            return username, password
        
username, password = prompts()

hashed_password = generate_password_hash(password)
bool_checkhash = check_password_hash(hashed_password, password)

print(f"Password matches hash? {bool_checkhash}")
print(f'"{username}" : "{hashed_password}" , ')
