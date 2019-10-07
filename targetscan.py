import socket
import subprocess
import os
import sys

def scan(trgtIP, ports):
    try:

        print('\n [+] Checking the availability of the Target : {}'.format(trgtIP))
        with open(os.devnull, "wb") as nothing:
            result = subprocess.Popen(["ping ", "-n ", "3 ", trgtIP], stdout=nothing, stderr=nothing).wait()
            if result == 0:
                print('\n [+] Target {} is online.'.format(trgtIP))
            else:
                print('\n [+] Target {} is offline.'.format(trgtIP))
        print('\n [+] Now scanning for ports......')

        for i in ports:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result1 = s.connect_ex(trgtIP, ports)
            if result1 == 0:
                print('\n [+] Port {} : Open')
            s.close()
    except KeyboardInterrupt:
        print('\n [-] You pressed Ctrl+C')
        sys.exit()
    except socket.error:
        print('\n [-] Could not connect to Port')
        sys.exit()

