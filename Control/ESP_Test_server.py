import socket
import struct
import errno
import keyboard

# General config
UDP_IP = "192.168.84.158"
UDP_PORT = 8888
MESSAGE_LENGTH = 7  # one data frame has 7 bytes

# Prepare UDP
print("This PC's IP: ", UDP_IP)
print("Listening on Port: ", UDP_PORT)
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setblocking(False)
sock.bind((UDP_IP, UDP_PORT))

take_input = True

def take_input():
    take_input = True


# Read data forever
while True:
    keyboard.on_press_key("s", lambda _:take_input)
    try:
        data, fromAddr = sock.recvfrom(MESSAGE_LENGTH)
        if data:
            if take_input:
                mode = int(input("Enter an int: "))
                speed1 = int(input("Enter speed1: "))
                speed2 = int(input("Enter speed2: "))
                sock.sendto(struct.pack('<hhh', mode, speed1, speed2), fromAddr)
                take_input = False

            Mode = struct.unpack_from('<B', data,0)
            # print("Received data: ", int.from_bytes(data, byteorder="big"))
            print("Mode: {}".format(Mode))

    except socket.error as why:
        if why.args[0] == errno.EWOULDBLOCK:
            pass  # No data received, continue listening
        elif why.args[0] == errno.WSAECONNRESET:
            print("Client forcibly closed the connection.")
        else:
            raise why

# Close the socket when done
sock.close()
print("Server terminated.")

