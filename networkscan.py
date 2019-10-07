import socket
import ipaddress
import subprocess
import os
import sys

def netscan(netaddr):
    netip = ipaddress.ip_network(netaddr)
    hostlist = netip.hosts()
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print('\n [+] Checking the availability of the Hosts.....')
        with open(os.devnull, "wb") as nothing:
            for i in hostlist:
                result = subprocess.Popen(["ping ", "-n ", "3 ", hostlist], stdout=nothing, stderr=nothing).wait()
                if result == 0:
                    print('\n [+] Target {} is online.'.format(trgtIP))
                else:
                    print('\n [+] Target {} is offline.'.format(trgtIP))

    except KeyboardInterrupt:
        print('\n [-] You pressed Ctrl+C')
        sys.exit()
    except socket.error:
        print('\n [-] Could not connect to Target')
        sys.exit()

