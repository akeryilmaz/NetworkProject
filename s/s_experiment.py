import socket
import time
import threading

def UDPClient(serverIP, serverPort, outputName):
    serverAddressPort = (serverIP, serverPort)
    # Create socket for sending packets to server.
    UDPClientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    packetsSent = 0
    # End-to-end delays list
    ETEDs = []
    # 1000 packets will be sent.
    while packetsSent < 1000:
        # The time at which the packet is sent to the server.
        startTime = time.time()
        # Send the packet to router r3
        UDPClientSocket.sendto(str(startTime).encode(), serverAddressPort)
        # Receive server d's response from router r3.
        message, _ = UDPClientSocket.recvfrom(1024)
        # The message received is the time at which d received the message we sent in string form.
        # Decode it and calculate the end-to-end-delay.
        ETED = 1000*(float(message.decode()) - startTime)
        ETEDs.append(ETED)
        packetsSent += 1
        print("Sent packet {}. ETED: {}".format(message, ETED))

    with open(outputName, "w") as f:
        for item in ETEDs:
            f.write(str(item) + "\n")

if __name__ == "__main__":
    # Create UDPClient and start sending messages.
    UDPClient("10.10.3.2", 4444, "End_to_end_delays2.txt")
