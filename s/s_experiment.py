import socket
import time
import threading

def UDPClient(serverIP, serverPort, outputName):
    serverAddressPort = (serverIP, serverPort)
    UDPClientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    packetsSent = 0
    ETEDs = []
    while packetsSent < 1000:
        startTime = time.time()

        UDPClientSocket.sendto(str(startTime).encode(), serverAddressPort)
        message, _ = UDPClientSocket.recvfrom(1024)

        ETED = 1000*(float(message.decode()) - startTime)
        ETEDs.append(ETED)
        packetsSent += 1
        print("Sent packet {}. ETED: {}".format(message, ETED))

    with open(outputName, "w") as f:
        for item in ETEDs:
            f.write(str(item) + "\n")

if __name__ == "__main__":
    UDPClient("10.10.3.2", 4444, "End_to_end_delays2.txt")
