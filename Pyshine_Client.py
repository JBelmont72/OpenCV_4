'''pyShine
https://www.youtube.com/watch?v=7-O7yeO3hNQ
Socket programming to send and receive webcam video
Go to the terminal window and run this command:

ipconfig getifaddr en0
my public IP address  75.68.100.114
That will show your LAN IP address. Note that en0 is commonly used for ethernet interface, and en1 is for the Airport interface. Make sure that your IP address is not starting from 127.x.x.x because that is your local host, and if you only want to check server client for the same pc then it is fine. Otherwise, consider using the command above and write the correct ip address for video transfer over different machines.
'''
# lets make the client code
import socket,cv2, pickle,struct

# create socket
client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# host_name  = socket.gethostname()
# host_ip = socket.gethostbyname(host_name)
# host_ip = '192.168.1.11' # paste your server ip address here
host_ip = '75.68.100.114'
host_ip ='192.168.1.12'
port = 9999
client_socket.connect((host_ip,port)) # a tuple
data = b""
payload_size = struct.calcsize("Q")
while True:
	while len(data) < payload_size:
		packet = client_socket.recv(4*1024) # 4K
		if not packet: break
		data+=packet
	packed_msg_size = data[:payload_size]
	data = data[payload_size:]
	msg_size = struct.unpack("Q",packed_msg_size)[0]
	
	while len(data) < msg_size:
		data += client_socket.recv(4*1024)
	frame_data = data[:msg_size]
	data  = data[msg_size:]
	frame = pickle.loads(frame_data)
	cv2.imshow("RECEIVING VIDEO",frame)
	key = cv2.waitKey(1) & 0xFF
	if key  == ord('q'):
		break
client_socket.close()