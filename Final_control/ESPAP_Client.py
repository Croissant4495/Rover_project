import socket
import struct
import errno
import keyboard
import Keyboard_handle

# General config
server_ip = "192.168.4.1"
server_port = 8888
MESSAGE_LENGTH = 8  # one data frame has 7 bytes

# Prepare UDP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((server_ip, server_port)) # connect to server's ip and a port number

take_input = True

# Read data forever
while True:
    if keyboard.is_pressed('s'):
         take_input = True
    
    # Send dat
    if take_input:
                mode = int(input("Enter an int: "))
                speed1 = int(input("Enter speed1: "))
                speed2 = int(input("Enter speed2: "))
                sock.send(struct.pack('<hhh', mode, speed1, speed2))
                take_input = False

    # Try recieving data
    # try:10
    #     data, fromAddr = sock.recvfrom(MESSAGE_LENGTH)
    #     if data:
    #         rcv_mode = struct.unpack_from('<h', data,0)
    #         print("Mode: {}".format(rcv_mode))

    # except socket.error as why:
    #     if why.args[0] == errno.EWOULDBLOCK:
    #         pass  # No data received, continue listening
    #     elif why.args[0] == errno.WSAECONNRESET:
    #         print("Client forcibly closed the connection.")
    #     else:
    #         raise why

# Close the socket when done
sock.close()
print("Server terminated.")

