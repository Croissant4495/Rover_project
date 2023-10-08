import socket
import struct
import errno
import time

# General config
UDP_IP = "192.168.1.9"  # Change to your ip
UDP_PORT = 8888
MESSAGE_LENGTH = 13  # one sensor data frame has 13 bytes

new_time = time.time()
old_time = 0
dt = 0

def prepare_udp() -> socket.socket:
    print("This PC's IP: ", UDP_IP)
    print("Listening on Port: ", UDP_PORT)
    sock = socket.socket(socket.AF_INET,
                        socket.SOCK_DGRAM)
    sock.setblocking(False)
    sock.bind((UDP_IP, UDP_PORT))
    return sock

class Gyro_data_frame:
    def __init__(self) -> None:
        self.speeds = [0, 0, 0]
        self.angles = [0, 0, 0]
    
    def speed_to_angle(self):
        print("DT:", dt)
        for i in range(3):
            self.angles[i] = self.angles[i] + self.speeds[i] * dt     

def recieve_data(sock:socket.socket, frame:Gyro_data_frame):
    flag = False
    try:
        data, fromAddr = sock.recvfrom(MESSAGE_LENGTH)
        if data:
            flag = True
            for i in range(3):
                frame.speeds[i] = struct.unpack_from('<f', data, 1 + i*4)[0]
            # print("received data: ", frame.speeds)

    except socket.error as why:
        if why.args[0] == errno.EWOULDBLOCK:
            pass  # No data received, continue listening
        elif why.args[0] == errno.WSAECONNRESET:
            print("Client forcibly closed the connection.")
        else:
            raise why
    return flag

def update_time():
    global old_time, new_time, dt
    old_time = new_time
    new_time = time.time()
    dt = new_time - old_time