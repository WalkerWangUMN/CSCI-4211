# ZhaoyuWang, Zhang CSCI4211, 20/04/2020

## Ethernet-Algorithm
* Data structure
  * Map from MAC address and SwitchID to the port numbers
* Purpose
  * send packets to the destination and record and inform to switch the interface
## Pseudocode
* function _handle_PacketIn(event):
  PortTable[src_mac + switchID] = packetInPort
  if dst_mac and switchID are not the key for the port table:
    send packet to all the ports except the src port
  else:
    require the switch to foraward packets to output port