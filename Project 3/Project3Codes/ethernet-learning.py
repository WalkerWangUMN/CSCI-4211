from pox.core import core
import pox.openflow.libopenflow_01 as of


# Even a simple usage of the logger is much nicer than print!
log = core.getLogger()


# !!!!! PROJ3 Define your data structures here

Table = {}

# Handle messages the switch has sent us because it has no
# matching rule.

def _handle_PacketIn (event):

  # get the port the packet came in on for the switch contacting the controller
  packetInPort = event.port

  # use POX to parse the packet
  packet = event.parsed

  # get src and dst mac addresses
  src_mac = str(packet.src)
  dst_mac = str(packet.dst)

  # get switch ID
  switchID = str(event.connection.dpid) + str(event.connection.ID)
  
  log.info('Packet has arrived: SRCMAC:{} DSTMAC:{} from switch:{} in-port:{}'.format(src_mac, dst_mac, switchID, packetInPort))

  # !!!!! PROJ3 Your logic goes here

  if src_mac + switchID not in Table:
    Table[src_mac+switchID] = packetInPort

  if dst_mac+switchID not in Table:
    log.info("Switch {}: [Unknown destination {}] <Flood operation>".format(switchID,dst_mac))
    message = of.ofp_packet_out()
    message.data = event.ofp
    message.in_port = packetInPort
    action = of.ofp_action_output(port =  of.OFPP_FLOOD)
    message.actions.append(action)
    event.connection.send(message)
  else:
    log.info("Data flow: {}.{} -> {}.{}".format(src_mac, packetInPort, dst_mac, Table[dst_mac+switchID]))
    message = of.ofp_flow_mod()
    message.data = event.ofp
    action = of.ofp_action_output(port = Table[dst_mac+switchID])
    message.actions.append(action)
    event.connection.send(message)

def launch ():
  core.openflow.addListenerByName("PacketIn", _handle_PacketIn)
  log.info("Pair-Learning switch running.")
