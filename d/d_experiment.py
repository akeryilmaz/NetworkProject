import socket
import time
import threading

def UDPServer(localIP, localPort):
    # Create UDP Server socket and bind local IP & port to it.
    UDPServerSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    UDPServerSocket.bind((localIP, localPort))
    print("UDP Server on IP {} is ready.".format(localIP))
    while True:
        # Listen for incoming packets.
        message, address = UDPServerSocket.recvfrom(1024)
        # The time at which the packet is received.
        endTime = time.time()
        # Send the time at which the packet is received back to the sender (router r3 in this case)
        UDPServerSocket.sendto(str(endTime).encode(), address)
        # print("Received message: ", message.decode(), " Sent message:", endTime, " diff: ", endTime-float(message.decode()))

if __name__ == "__main__":
    # Start listening for messages coming from r3 as a UDPServer.
    UDPServer("10.10.7.1", 4444)
