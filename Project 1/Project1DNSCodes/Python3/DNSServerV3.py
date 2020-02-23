# Spring 2020 CSci4211: Introduction to Computer Networks
# This program serves as the server of DNS query.
# Written in Python v3.

import sys, threading, os, random, subprocess
from socket import *

def main():
	host = "localhost" # Hostname. It can be changed to anything you desire.
	port = 9889 # Port number.

	#create a socket object, SOCK_STREAM for TCP
	sSock = socket(AF_INET, SOCK_STREAM)
	#bind socket to the current address on port 5001
	sSock.bind((host, port))
	#Listen on the given socket maximum number of connections queued is 20
	sSock.listen(20)

	monitor = threading.Thread(target=monitorQuit, args=[])
	monitor.start()

	print("Server is listening...")

	while 1:
		#blocked until a remote machine connects to the local port 5001
		connectionSock, addr = sSock.accept()
		server = threading.Thread(target=dnsQuery, args=[connectionSock, addr[0]])
		server.start()

def dnsQuery(connectionSock, srcAddress):
	#check the DNS_mapping.txt to see if the host name exists
	#set local file cache to predetermined file.
        #create file if it doesn't exist 
        #if it does exist, read the file line by line to look for a
        #match with the query sent from the client
        #If match, use the entry in cache.
            #However, we may get multiple IP addresses in cache, so call dnsSelection to select one.
	#If no lines match, query the local machine DNS lookup to get the IP resolution
	#write the response in DNS_mapping.txt
	#print response to the terminal
	#send the response back to the client
	#Close the server socket.
	try:
		f = open("DNS_Mapping.txt", 'r')
	except error:
		nF = open("DNS_Mapping.txt", 'w')
		nF.close()
		f = open("DNS_Mapping.txt", 'r')
	data = connectionSock.recv(1024).decode()
	try:
		record = f.readline()
		check = False
		while record != '':
			record = record.split(':')
			if record[0] == data:
				check = True
				if (record[-1] == "Host Not Found"):
					message = "Host Not Found"
				else:
					message = "Local DNS: " + data + ':' + dnsSelection(record[1:])
			record = f.readline()
		f.close()
		if not check:
			message = "Root DNS: " + data + ':' + gethostbyname(data)
			f = open("DNS_Mapping.txt", 'a')
			f.write(data+','+ gethostbyname(data) + '\n')
			f.close()
	except:
		message = "Root DNS: " + data + ":Host Not Found"
		f = open("DNS_Mapping.txt", 'a')
		f.write(data+",Host Not Found\n")
		f.close()
	#print response to the terminal
	print(message)
	#send the response back to the client
	connectionSock.send(message.encode())	
	#Close the server socket.
	connectionSock.close()
  
def dnsSelection(ipList):
	#checking the number of IP addresses in the cache
	#if there is only one IP address, return the IP address
	#if there are multiple IP addresses, select one and return.
	##bonus project: return the IP address according to the Ping value for better performance (lower latency)
	if ipList[1:] == []:
		return ipList[0]
	else:
		re = []
		for i in range(len(ipList)):
			output = subprocess.check_output("ping -c 1 " + ipList[i],shell=True).decode()
			re.append(float(output.split("time=")[1].split(" ")[0]))
		i = re.index(min(re))
		return ipList[i]

def monitorQuit():
	while 1:
		sentence = input()
		if sentence == "exit":
			os.kill(os.getpid(),9)

main()
