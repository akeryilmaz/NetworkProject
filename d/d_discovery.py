import socket
import time
import threading

def UDPServer(localIP, localPort):
    # Create UDP Server socket and bind local IP & port to it.
    UDPServerSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    UDPServerSocket.bind((localIP, localPort))
    while True:
        print("UDP Server on IP {} is ready.".format(localIP))
        # Listen for incoming packets and echo back.
        message, address = UDPServerSocket.recvfrom(1024)
        UDPServerSocket.sendto(message, address)

if __name__ == "__main__":
    interfaceIPs = {"r1": "10.10.4.2", "r2": "10.10.5.2", "r3": "10.10.7.2"}
    threads = []
    for key in interfaceIPs.keys():
        t = threading.Thread(target=UDPServer, args=(interfaceIPs[key], 4444))
        threads.append(t)
    for t in threads:
        t.start()
    for t in threads:
        t.join()