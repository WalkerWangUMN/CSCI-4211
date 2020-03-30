# CSCI4211_rdt_python

How to run:
* install Python 3
* change directory to the root directory
* run "python3 main.py" in command line

Test cases:
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

Data structure:


Function:
* For Alternating-Bit-Protocol Version:
    * A_timerinterrupt(), A_output(), A_input(), A_init(), B_input(), and B_init() implement a stop-and-wait for transferring data from A-side to  B-side. The protocol uses both ACK and NACK messages.
