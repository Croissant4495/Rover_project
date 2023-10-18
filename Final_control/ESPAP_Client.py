import WiFi
my_ip = "192.168.1.1"
# sock = WiFi.start_socket_server(my_ip)
sock = WiFi.start_socket()
    
# Program Loop
while True:    
    data = WiFi.update_data()
    WiFi.send_data(sock, data)

