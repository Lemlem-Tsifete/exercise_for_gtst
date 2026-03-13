import socket


def get_info():
   
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    my_ip = s.getsockname()[0]
    s.close()

    first_part = int(my_ip.split('.')[0])

    if first_part < 128:
        ip_class = "Class A (Big network)"
    elif first_part < 192:
        ip_class = "Class B (Medium network)"
    else:
        ip_class = "Class C (Small/Home network)"

    print(f"My IP: {my_ip}")
    print(f"My Network Type: {ip_class}")

get_info()