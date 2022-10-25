# Very simple password strength tester and checker.
# Supplied with a list of common and predictable passwords like P4ssword1, admin, qwerty etc.

import re

password = str(input(f'[i] Welcome to the PassKeeper! Please enter a password that you would like to check >> '))

special_chars = re.compile('[@_!#$%^&*()<>?/\|}{~:]')

def password_validator(pw):

    with open('common.txt', 'r') as passlist:

        if len(pw) < 8 or pw in passlist == True:
            pw = str(input(f'[X] Password {pw} is too short (minimum 8 characters) or forbidden. Please enter a new password >> '))
            
        else:

            if len(pw) >= 8:
                print(f'[V] Good! Password is at least 8 characters long.')
                
                if(special_chars.search(pw) == None):
                    print(f'[X] No special characters! Try again!')
                    
                else:
                    print(f'[V] Special characters found!')

                    if bool(re.match(r'\w*[A-Z]\w*', pw)):
                        print(f'[V] Uppercase found!')                   
                        print(f'Great! Your password meets all the criteria -> (minimum 8 characters/has special characters/is not common).')

                    else:
                        print(f'[X] Your password does not contain uppercase.')
        

password_validator(password)
