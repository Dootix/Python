# ////////////////////////
# ************************
#
# Simple banner grabber for FTP, SMTP and MySQL.
#
# ************************
# ////////////////////////

import socket

PORTS = [21,25,3306]

def banner_grabber(IP, port):
    
    for i in range(0,3):
        
        try:
            port = PORTS[i]
            print(f'Banner for port {port}')
            s = socket.socket()
            s.connect((IP, port))
            s.settimeout(2)
            answer = s.recv(1024)
            s.close()
            print(answer)
            
        except:
            return 'ERROR'
        
        continue
    
def main():
    
    IP = input('Please provide IP of the target: ')
    banner_grabber(IP, PORTS)

main()
