import socket
import time
import threading

def UDPClient(serverIP, serverPort, outputName):
    serverAddressPort = (serverIP, serverPort) # ServerAddressPort : Server ip and port addresses of s,d or r2.
    UDPClientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # Create a UDP socket to send messages to server.
    with open("messages_r3.txt", "r") as f:
        packetsSent = 0
        totalRTT = 0
        while packetsSent < 1000:
            message = f.readline() # Get texts from "messages_r3.txt" line by line.
            startTime = int(round(time.time() * 1000)) # Starting time (the time at which the message is sent) in ms.
            UDPClientSocket.sendto(message.encode(), serverAddressPort) # Encode the message and send it to server.
            UDPClientSocket.recvfrom(1024) # Receive the feedback response from the server (this call waits until server sends a response back to us).
            endTime = int(round(time.time() * 1000)) # End time (the time at which the feedback message is received) in ms.
            totalRTT += endTime - startTime # Add RTT of this message which is (end-start) to the total RTT.
            packetsSent += 1
            #print("Sent packet {}. RTT: {}".format(message, endTime-startTime))

    # When done, write the output to the files "<s,r2,d>.txt"
    with open(outputName, "w") as f:
        f.write("Calculated RTT: {}".format(totalRTT/1000))

if __name__ == "__main__":
    destinations = {'s' : "10.10.3.1", 'r2': '10.10.6.1', 'd': "10.10.7.1"} # IP addresses for the servers in s,r2,d.
    sources = {'s': "10.10.3.2", 'r2': "10.10.6.2", 'd': "10.10.7.2"} # IP addresses of interfaces on our side for s,r2,d. (not used in this case)
    # Start sending strings defined in "messages_r3.txt" to s,r2,d from different threads, from port 4444.
    threads = []
    for key in destinations.keys():
        t = threading.Thread(target=UDPClient, args=(destinations[key], 4444, key+"_link_cost.txt"))
        threads.append(t)
    for t in threads:
        t.start()
    for t in threads:
        t.join()
