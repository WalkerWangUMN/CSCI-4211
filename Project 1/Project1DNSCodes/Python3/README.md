# Zhaoyu Wang, Zhang CSCI4211, 23/02/2020

### Compilation
* Server:
	* Run:
  		* "python3 DNSServerV3.py" to start the server side.<br/>
        	* Enter "exit" to quit the server.<br/>
* Client:
	* Run:
        	* 'python3 DNSClientV3.py' to start the client side.<br/>
		* Enter 'q' or 'Q' to exit the client.<br/>

### Execution
Server:
    Run:
        "python3 DNSServerV3.py" to start the server side.<br/>
        Enter "exit" to quit the server.<br/>
Client:
    Run:
        'python3 DNSClientV3.py' to start the client side.<br/>
		Enter 'q' or 'Q' to exit the client.<br/>

### Description   
The client send query(input) to the server. The server would check the DNS_mapping.txt first to see whether host name exits and set this local file cache to predetermined file. If it exists, read the file line by line to look for match with the query from client. If not, the program will creates file. If match, use the entry in cache and call dnsSelection to select one from multiple IP addresses in cache. If not, query the local machine DNS lookup to get the IP resolution. Finally, the program writes the response in DNS_mapping.txt, prints response to the terminal, sends the response back to the client and closes the server socket.
