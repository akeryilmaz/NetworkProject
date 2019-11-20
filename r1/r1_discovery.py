import socket
import time
import threading

def UDPClient(serverIP, serverPort):
    serverAddressPort = (serverIP, serverPort)
    UDPClientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    with open("messages_r1.txt", "r") as f:
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

if __name__ == "__main__":
    destinations = {'s' : "10.10.1.1", 'r2': '10.10.8.2', 'd': "10.10.4.2"}
    sources = {'s': "10.10.1.2", 'r2': "10.10.8.1", 'd': "10.10.4.1"}
    # Start sending to s,r2,d from different threads.
    threads = []
    for key in destinations.keys():
        t = threading.Thread(target=UDPClient, args=(destinations[key], 4444))
        threads.append(t)
    for t in threads:
        t.start()
    for t in threads:
        t.join()