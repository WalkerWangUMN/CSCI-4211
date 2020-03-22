from pj2.simulator import to_layer_five
from pj2.packet import send_ack

class B:
    def __init__(self):
        # TODO: initialization of the state of B
        # self.seq
        # ...
        self.expect_seq = 1
        self.packet_to_send.seqnum = -1
        self.packet_to_send.acknum = 0
        memset(self.packet_to_send.payload, 0, 20)
        self.packet_to_send.checksum = get_checksum(&self.packet_to_send)
        return

    def B_input(self, pkt):
        # TODO: process the packet recieved from the layer 3
        # verify checksum
        # send ACK
        if pkt.checksum != pkt.get_checksum():
            to_layer_three("B", pkt)
            return
        if pkt.seqnum != self.expect_seq:
            to_layer_three("B", pkt)
            return
        to_layer_five("B", pkt.payload.data)
        self.packet_to_send.acknum = self.expect_seq
        self.packet_to_send.checksum = self.packet_to_send.get_checksum()
        to_layer_three("B", pkt)
        return

    def B_output(self, m):
        return

    def B_handle_timer(self):
        return


b = B()
