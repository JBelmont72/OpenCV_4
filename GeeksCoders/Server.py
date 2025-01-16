'''

'''
## NeuralNine Connect sockets via internet
import socket
server=socket.socket(socket.AF_INET,socket.SOCK_STREAM,0)
# server.bind(('127.0.0.1',9999))
server.bind(('192.168.1.11',9999))
server.listen()
print('listening...')
while True:
    client,addr=server.accept()
    client.send('Hello Client!'.encode('utf-8'))
    print(client.recv(1024).decode('utf-8'))



# import socket
# import sys
# def main():
#     try:
#         client_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM,0)
#     except socket.error as e:
#         print('Falied to create a socket')
#         print(f'Reason: {e}')
#         sys.exit()
#     print('Socket Created Successfully')

#     targetHost=input('Please enter the target host name')
#     targetPort=input('Please enter target port: ')

#     try:
#         client_socket.connect((targetHost,int(targetPort)))
#         print(f"Socket connected to host {targetHost} on Port {targetPort}")
#         client_socket.shutdown(2)
#     except socket.error as e:
#         print(f"error connecting to {targetHost}")
#         print(f'Error: {e}')
        
# if __name__=='__main__':
#     main()
    
## to convert ip address to hexadecimal   
# import socket
# from binascii import hexlify
# def convert_ip():
#     for ip_addr in ['127.0.0.1', '192.168.0.1']:
#         packed_ip_addr = socket.inet_aton(ip_addr)
#         unpacked_ip_addr = socket.inet_ntoa(packed_ip_addr)


#         print("IP Address : {} => Packed: {}, Unpacked: {} " .format(ip_addr, hexlify(packed_ip_addr), unpacked_ip_addr))

# convert_ip()
########~~~~~
# import socket
# def socket_time_out():
#     s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     print('Default Socket Timeout', s.gettimeout(), s.settimeout(100))
#     print('Current Socket Timeout', s.gettimeout())


# socket_time_out()
##~~~~~~~~to get time from ntp
# import ntplib## i did not install module

# def print_time():
#     ntpClient=ntplib.NTPClient()
#     response=ntpClient.request('pool.ntp.org')
#     print(ctime(response.tx_time))
# if __name__=='__main__':
#     print_time()