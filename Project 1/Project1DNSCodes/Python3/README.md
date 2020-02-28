# Zhaoyu Wang, Zhang CSCI4211, 23/02/2020

### Compilation
* Server:
	* Run:
  		* "python3 DNSServerV3.py" to start the server side.
		* Enter "exit" to quit the server.
* Client:
	* Run:
		* "python3 DNSClientV3.py" to start the client side.
		* Enter 'q' or 'Q' to exit the client.

### Execution
* Open two terminals
* First terminal
	* Use "python3 DNSServerV3.py" and push return to start the server side 
	* There will be "Server is listening ..." in the terminal and continue the second terminal
	* There will be "domain name,IP address" in the terminal after you type the domain name in second terminal
	* Enter "exit" and push return to quit the server if you want to kill the server side.
* Second terminal
	* Use "python3 DNSClientV3.py" and push return to start the client side.
	* There will be "Type in a domain name to query, or 'q' to quit" in the terminal
	* Type the domain name to get the IP address
	* Enter 'q' or 'Q' to exit the client if you want to kill client side

### Description   
* main() function will create socket which is listening to the client and then the function will call dnsQuery() when it received a query. Maximum number of connections queued is 20.
* dnsQuery() function will parse query and send back query result and split the query by ':'. If it exists in cache, the function will return the IP in cache and then call dnsSelection() for selecting one from multiple IP addesses in cache. If not, the function will query the local machine DNS lookup to get the IP resolution and save the record. If not found, the function will tell host not found. Finally, the function will write response in DNS_mapping.txt, send the response and then close the sock.
* dnsSelection() function will return the IP address if there are one or more ipaddresses.
* monitorQuit() function will kill the program if there is "exit" in the terminal.