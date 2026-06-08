
from typing import Any
import re

'''
def addressVal(address):
    dot = address.find(".")
    at = address.find("@")
    if (dot == -1):
        print("Invalid")
    elif (at == -1):
        print("Invalid")
    else:
        print("Valid")

print("This program will decide if your input is a valid email address")
while(True):
    print("A valid email address needs an '@' symbol and a '.'")
    x = input("Input your email address:")

    addressVal(x)
'''
def email_validate(
        prompt:str,
        error_message:str,
        pattern:str,   
        strip:bool = False,
        lower:bool = False,
        )->str:
            '''
            This function will Using re validate to strong validate the input -> return str email
            and its can reuse for phone, name ,address by change the pattern.
            if try with validate number cant also expand more agriument: min_value,max_value or convert...
            '''
                while True:
                    try:
                        email = input(prompt).strip() if strip else input(prompt)
                        email = email.lower() if lower else email
                        if not re.match(pattern,email):
                            raise ValueError
                        else:
                            return email         
                               
                    except ValueError as e:
                        print(f'{error_message} {e}')
               
def main():     
    email = email_validate(
                prompt='Please enter your Email Address: ',
                error_message='Invalid Email. Try again!!',
                pattern = r'^[a-zA-Z0-9._]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,}$',
                strip=True,
                lower=True
                )

    print(f'Your Email: {email}')
    
if __name__ == "__main__":
    main()
