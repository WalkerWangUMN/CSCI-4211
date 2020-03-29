from pj2.simulator import to_layer_five
from pj2.packet import send_ack


class B:
    def __init__(self):
        # go back n, the initialization of B
        # The state only need to maintain the information of expected sequence number of packet
        self.expect_seq = 1
        self.packet_to_send.seqnum = -1
        self.packet_to_send.acknum = 0
        memset(self.packet_to_send.payload, 0, 20)
        self.packet_to_send.checksum = self.packet_to_send.get_checksum()
        return

    def B_output(self, m):
        return

    def B_input(self, pkt):
        # go back n, B_input
        # You need to verify the checksum to make sure that packet isn't corrupted
        # If the packet is the right one, you need to pass to the fifth layer using "to_layer_five(entity,payload)"
        # Send acknowledgement using "send_ack(entity, seq)" based on the correctness of received packet
        # If the packet is the correct one, in the last step, you need to update its state ( update the expected sequence number)
        if pkt.checksum != pkt.get_checksum():
            to_layer_three("B", self.packet_to_send)
            return
        if pkt.seqnum != self.expect_seq:
            to_layer_three("B", self.packet_to_send)
            return
        to_layer_five("B", pkt.payload)
        self.packet_to_send.acknum = self.expect_seq
        self.packet_to_send.checksum = self.packet_to_send.get_checksum()
        to_layer_three("B", self.packet_to_send)
        self.expect_seq += 1
        return

    def B_handle_timer(self):
        return


b = B()
