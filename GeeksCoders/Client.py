'''Parwiz Forogh
https://www.youtube.com/watch?v=JaWXHHIDddE&list=PL1FgJUcJJ03uh-PXb9Cmr6qLd3gyZHIW7&index=2
'''
import socket
from socket import AF_INET,SOCK_STREAM
client_socket=socket.socket(family=AF_INET,type=SOCK_STREAM,proto=0)
# print(f'Socket created{server_socket}')

def main():
    hostname=socket.gethostname()
    ipaddr=socket.gethostbyname(hostname)
    print(f'Host Name is: {hostname}')
    print(f'IP address is: {ipaddr}')
    # client_socket.connect(('127.0.0.1',9999))
    client_socket.connect(('192.168.1.11',9999))
    print(client_socket.recv(1024).decode('utf-8'))
    client_socket.send('Hello Server'.encode('utf-8'))
if __name__=='__main__':
    main()
