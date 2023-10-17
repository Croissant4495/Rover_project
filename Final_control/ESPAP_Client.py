import WiFi
sock = WiFi.start_socket()
    
# Program Loop
while True:    
    WiFi.send_data(sock)

