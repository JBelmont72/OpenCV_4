import socket
def main():
    remote_host = 'www.geekscoders.com' ## codeloop.org python.org
 
    try:
        print("IP Address Of " + remote_host + " is " + socket.gethostbyname(remote_host))
 
    except socket.error as e:
        print("Error " , e)
 
 
 
 
if __name__ == "__main__":
    main()

# import sys
 
 
# def main():
#     try:
#         s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
 
#     except socket.error as e:
#         print("Failed To Create A Scoket")
#         print("Reason : ", str(e))
#         sys.exit()
 
#     print("Socket Created Successfully")
 
#     targetHost = input("Please enter target host name to connect: ")
#     targetPort = input("Please enter target port : ")
 
#     try:
#         s.connect((targetHost, int(targetPort)))
#         print("Socket connected to host " + targetHost + " on port " + targetPort)
#         s.shutdown(2)
 
 
#     except socket.error as e:
#         print("Failed connection to host " + targetHost + " on port " + targetPort)
#         print("Reason", str(e))
#         sys.exit()
 
 
 
 
 
# if __name__ == "__main__":
#     main()
    
import socket
 
 
def main():
    hostName = socket.gethostname()
 
    ipaddr = socket.gethostbyname(hostName)
    print(" Host Name Is : {} " .format(hostName))
    print(" IP Address Is : {} " .format(ipaddr))
    # ##help(socket.gethostname)
 
 
 
if __name__ == "__main__":
    main()