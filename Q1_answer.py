import socket

target_ip = "127.0.0.1" 
for port in range(75, 85):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)

    result = sock.connect_ex((target_ip, port))
    
    if result == 0:
        print(f"Success! Port {port} is OPEN.")
    else:
        print(f"Port {port} is closed.")
        
    sock.close()