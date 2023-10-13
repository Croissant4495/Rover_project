import socket
import struct
import errno
import Keyboard_handle
import line_track

# General config
server_ip = "192.168.4.1"
server_port = 8888
MESSAGE_LENGTH = 8  # one data frame has 8 bytes

# Prepare TCP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((server_ip, server_port)) # connect to server's ip and a port number

# Recieve
def recieve()->int:
    try:
        rcv_data, fromAddr = sock.recvfrom(MESSAGE_LENGTH)
        if data:
            data = struct.unpack('<h', rcv_data)
            print("Distance: {}".format(data))
            return data

    except socket.error as why:
        if why.args[0] == errno.EWOULDBLOCK:
            pass  # No data received, continue listening
        elif why.args[0] == errno.WSAECONNRESET:
            print("Client forcibly closed the connection.")
        else:
            raise why

# Read data forever
while True:    
    # Send data
    data_arr = Keyboard_handle.decide_mode()
    if data_arr[0] == 5:
        line_track.move_line()
    else:
        sock.send(struct.pack('<hhhh', *data_arr))

    # Try recieving data
    try:
        us_distance = recieve()
    except:
        pass

# Close the socket when done
sock.close()
print("Server terminated.")

