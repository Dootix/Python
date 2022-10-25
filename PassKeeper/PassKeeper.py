# Very simple password strength tester and checker.
# Supplied with a list of common and predictable passwords like P4ssword1, admin, qwerty etc.
# created by Dootix

import re

# Declaring password variable that is provided by the user and regex compiler with special characters for later check.
password = str(input(f'[i] Welcome to the PassKeeper! Please enter a password that you would like to check >> '))
special_chars = re.compile('[@_!#$%^&*()<>?/\|}{~:]')

def password_validator(pw):

    # Opening a file with common passwords that should not be allowed.
    with open('common.txt', 'r') as passlist:
        
        # Checking if password is shorter than 8 chars and if password is on the common passwords list. 
        if len(pw) < 8 or pw in passlist == True: 
            pw = str(input(f'[X] Password {pw} is too short (minimum 8 characters) or forbidden. Please enter a new password >> '))
            
        else:
            
            # If password is longer than 8 characters and printing the confirmation.
            if len(pw) >= 8: 
                print(f'[V] Good! Password is at least 8 characters long.')
                
                # Checking if password has at least one special character.
                if(special_chars.search(pw) == None):
                    print(f'[X] No special characters! Try again!')
                    
                else:
                    print(f'[V] Special characters found!')
                    
                    # Checking if password has at least one uppercase.
                    if bool(re.match(r'\w*[A-Z]\w*', pw)):
                        print(f'[V] Uppercase found!')                   
                        print(f'Great! Your password meets all the criteria -> (minimum 8 characters/has special characters/is not common).')

                    else:
                        print(f'[X] Your password does not contain uppercase.')
        

password_validator(password)
