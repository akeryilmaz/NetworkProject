import socket
import time
import threading

def UDPServer(localIP, localPort):
    # Create UDP Server socket and bind local IP & port to it.
    print("Trying to create socket with {} and {}".format(localIP, localPort))
    UDPServerSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    UDPServerSocket.bind((localIP, localPort))
    print("UDP Server on IP {} is ready.".format(localIP))
    while True:
        # Listen for incoming packets and echo back.
        message, address = UDPServerSocket.recvfrom(1024)
        UDPServerSocket.sendto(message, address)
        print("Received message: {}", message.decode())

if __name__ == "__main__":
    interfaceIPs = {"r1": "10.10.1.1", "r2": "10.10.2.2", "r3": "10.10.3.1"}
    threads = []
    for key in interfaceIPs.keys():
        t = threading.Thread(target=UDPServer, args=(interfaceIPs[key], 4444))
        threads.append(t)
    for t in threads:
        t.start()
    for t in threads:
        t.join()
