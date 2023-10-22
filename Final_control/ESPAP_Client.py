import WiFi

sock = WiFi.start_socket()
# sock = WiFi.start_socket()
    
# Program Loop
while True: 
    data = WiFi.update_data()
    print(data)
    WiFi.send_data(sock, data)

