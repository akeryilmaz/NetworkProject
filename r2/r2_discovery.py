import socket
import time
import threading

def UDPClient(serverIP, serverPort):
    serverAddressPort = (serverIP, serverPort)
    UDPClientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    with open("messages_r2.txt", "r") as f:
        packetsSent = 0
        totalRTT = 0
        while packetsSent < 1000:
            message = f.readline()
            startTime = int(round(time.time() * 1000))
            UDPClientSocket.sendto(message.encode(), serverAddressPort)
            UDPClientSocket.recvfrom(1024)
            endTime = int(round(time.time() * 1000))
            totalRTT += endTime - startTime
            packetsSent += 1
            print("Sent packet {}. RTT: {}".format(message, endTime-startTime))
    print("Calculated RTT: {}".format(totalRTT/1000))

def UDPServer(localIP, localPort):
    # Create UDP Server socket and bind local IP & port to it.
    UDPServerSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    UDPServerSocket.bind((localIP, localPort))
    print("UDP Server on IP {} is ready.".format(localIP))
    while True:
        # Listen for incoming packets and echo back.
        message, address = UDPServerSocket.recvfrom(1024)
        UDPServerSocket.sendto(message, address)
        print("Received message {}".format(message))


if __name__ == "__main__":
    destinations = {'s' : "10.10.2.2", 'r1': '10.10.8.1', 'd': "10.10.5.2", 'r3': "10.10.6.2"}
    sources = {'s': "10.10.2.1", 'r1': "10.10.8.2", 'd': "10.10.5.1", 'r3': "10.10.6.1"}
    # Echo back to r1 & r3 (Server). Send packets to s and d (Client).
    s = threading.Thread(target=UDPClient, args=(destinations['s'], 4444))
    d = threading.Thread(target=UDPClient, args=(destinations['d'], 4444))
    r1 = threading.Thread(target=UDPServer, args=(sources['r1'], 4444))
    r3 = threading.Thread(target=UDPServer, args=(sources['d'], 4444))

    r1.start()
    r3.start()
    d.start()
    s.start()
    s.join()
    d.join()
    r1.join()
    r3.join()