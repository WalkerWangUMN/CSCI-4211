# CSCI4211_rdt_python

### How to run:
* install Python 3
* change directory to the root directory
* run "python3 main.py" in command line

### Test cases:
* No loss and no error scenario to demonstrate that the code works under no error case:
    * Enter the number of messages to simulate: 10
    * Enter packet loss probability [enter 0.0 for no loss]: 0.0
    * Enter packet corruption probability [0.0 for no corruption]: 0.0
    * Enter average time between messages from sender's layer5 [ > 0.0]: 5.0
    * Enter TRACE: 0
* 30 percent loss and no error scenario to demonstrate the code can recover the lossed packets:
    * Enter the number of messages to simulate: 50
    * Enter packet loss probability [enter 0.0 for no loss]: 0.3
    * Enter packet corruption probability [0.0 for no corruption]: 0.0
    * Enter average time between messages from sender's layer5 [ > 0.0]: 10.0
    * Enter TRACE: 0
* No loss and 30 percent corruption scenario to demonstrate the code can recover the erroneously received packets:
    * Enter the number of messages to simulate: 10
    * Enter packet loss probability [enter 0.0 for no loss]: 0.0
    * Enter packet corruption probability [0.0 for no corruption]: 0.3
    * Enter average time between messages from sender's layer5 [ > 0.0]: 10.0
    * Enter TRACE: 0

### Data structure:
* packet, seq used to indicate the status, state used to indicate the state, estimated_rtt used to indicate the state of timer

### Function:
* A_timerinterrupt(), A_output(), A_input(), A_init(), B_input(), and B_init() implement a stop-and-wait for transferring data from A-side to  B-side. The protocol uses both ACK and NACK messages.
* B_init()
    * initialization of B
* B_input() 
    * verify the checksum and acknowlegement number
    * send packet to the fifth layer and acknowlegement
    * update the expected sequence number
* A__init__()
    * initialization of A
* A_input()
    * verify the checksum and acknowlegement number
    * stop timer
    * update the status of A
* A_output()
    * verify the status of A
    * construct the packet
    * send the packet using to_layer_three
    * save the packet
    * set the timer
* A_handler_timer
    * verify the status of A
    * send the packet using to_layer_three
    * set the timer