import socket

def resolvehost(hostname):
    global trgtIP
    try:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        trgtIP = socket.gethostbyname(hostname)
    except:
        print('[+] Could not resolve Host')

