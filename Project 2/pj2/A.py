from pj2.simulator import sim
from pj2.simulator import to_layer_three
from pj2.event_list import evl
from pj2.packet import *
from pj2.circular_buffer import circular_buffer

class A:
    def __init__(self):
        # TODO: initialization of the state of A
        # self.estimated_rtt
        # ...
        self.base = 1
        self.nextseq = 1
        self.window_size = 8
        self.estimated_rtt = 15
        self.buffer_next = 1
        return

    def A_input(self, pkt):
        # TODO: recive data from the other side
        # process the ACK, NACK from B
        if pkt.checksum != get_checksum(pkt): return
        if pkt.acknum < self.base: return
        self.base = self.acknum + 1
        if self.base == self.nextseq:
            # stoptimer(0)
            # send_window()
        else: self.start_timer("A", self.estimated_rtt)
        return

    def A_output(self, m):
        # TODO: called from layer 5, pass the data to the other side
        pkt = packet(seqnum=self.seq, payload=m)
        to_layer_three("A", pkt)

    def A_handle_timer(self):
        # TODO: handler for time interrupt
        # resend the packet as needed
        i = self.base
        while i < self.nextseq:

            i += 1

        self.start_timer("A", self.estimated_rtt)
        return


a = A()
