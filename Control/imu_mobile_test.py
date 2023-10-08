from imu_mobile_utils import *
import socket
import struct
import errno

sock = prepare_udp()
frame = Gyro_data_frame()

# Read data forever
while True:
    update_time()
    flag = recieve_data(sock, frame)
    if flag:
        print("received data: ", frame.speeds)
        frame.speed_to_angle()
        print(frame.angles)
