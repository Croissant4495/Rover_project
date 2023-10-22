import socket
import struct
import errno
import Keyboard_handle
import line_track

# General config
server_ip_default = "192.168.4.1"
server_port = 8888
MESSAGE_LENGTH = 8  # one data frame has 8 bytes


# Prepare TCP client
def start_socket():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((server_ip_default, server_port)) # connect to server's ip and a port number
    return sock

# Prepare TCP server
def start_socket_server():
    server_ip = socket.gethostbyname(socket.gethostname())
    print()
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # sock.setblocking(False)
    sock.bind((server_ip, server_port))
    print("IP and Port: ", server_ip, " ", server_port)
    sock.listen(5)
    return sock


# Recieve
def recieve(sock: socket.socket):
    try:
        rcv_data, fromAddr = sock.recvfrom(MESSAGE_LENGTH)
        if data:
            data = struct.unpack('<c', rcv_data)
            print("Distance: {}".format(data))
            return data, fromAddr            

    except socket.error as why:
        if why.args[0] == errno.EWOULDBLOCK:
            pass  # No data received, continue listening
        elif why.args[0] == errno.WSAECONNRESET:
            print("Client forcibly closed the connection.")
        else:
            raise why
        return [-1, -1]
    
def recv_server(sock: socket.socket):
    try:
        client_socket, client_ip = sock.accept()
        print( "Client ip: ", client_ip)
        data = client_socket.recv(MESSAGE_LENGTH)
        return data, client_ip

    except socket.error as why:
        if why.args[0] == errno.EWOULDBLOCK:
            pass  # No data received, continue listening
        elif why.args[0] == errno.WSAECONNRESET:
            print("Client forcibly closed the connection.")
        else:
            raise why
        return [-1, -1]
    

        

def update_data():
    # update data_arr
    data = Keyboard_handle.decide_mode()
    if data[0] == 5:
        data = line_track.move_line()
    return data


# def send_data(sock:socket.socket, data, address):
#     # Send data
#     sock.sendto(struct.pack('<hhhh', *data), address)

def send_data(sock:socket.socket, data):
    # Send data
    sock.send(struct.pack('<hhhh', *data))
    
