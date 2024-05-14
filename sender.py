from socket import *
from util import *

RECEIVER_ADDRESS = ('', 10185)
BUFFER_SIZE = 1024
SLEEP_DURATION = 3


class Sender:
    def __init__(self):
        """ 
        Your constructor should not expect any argument passed in,
        as an object will be initialized as follows:
        sender = Sender()
        
        Please check the main.py for a reference of how your function will be called.
        """
        self.seq_num = 0
        self.packet_counter = 0

    def rdt_send(self, app_msg_str):
        """realibly send a message to the receiver (MUST-HAVE DO-NOT-CHANGE)

        Args:
          app_msg_str: the message string (to be put in the data field of the packet)

        """
        print(f"\noriginal message string: {app_msg_str}")
        packet = make_packet(app_msg_str, 0, self.seq_num)
        print(f"packet created: {packet}")
        self.send_packet(packet, app_msg_str)

    ####### Your Sender class in sender.py MUST have the rdt_send(app_msg_str)  #######
    ####### function, which will be called by an application to                 #######
    ####### send a message. DO NOT change the function name.                    #######
    ####### You can have other functions if needed.                             #######

    def send_packet(self, packet, app_msg_str):
        """
        Sends a packet to the receiver, waits for an acknowledgment, and handles retransmissions if necessary.
        Args:
            packet (bytes): The packet data to be sent.
            app_msg_str (str): The application message string being sent, used for logging.
        """
        sender_socket = socket(AF_INET, SOCK_DGRAM)
        sender_socket.settimeout(SLEEP_DURATION)
        sender_socket.sendto(packet, RECEIVER_ADDRESS)
        self.packet_counter += 1
        print(f"packet num.{self.packet_counter} is successfully sent to the receiver.")

        try:
            received_packet, _ = sender_socket.recvfrom(BUFFER_SIZE)
            if verify_checksum(received_packet):
                ack_num = extract_ack_seq(received_packet)
                if self.seq_num == ack_num:
                    print(f"packet is received correctly: seq. num {self.seq_num} = ACK num {ack_num}. all "
                          f"done!\n")
                    self.seq_num = 1 - self.seq_num  # Toggle sequence number

                else:
                    print("receiver acked the previous pkt, resend!\n")
                    print(f"\n[ACK-Previous retransmission]: {app_msg_str}")
                    self.send_packet(packet, app_msg_str)

        except timeout:
            print("socket timeout! Resend!\n")
            print(f"[timeout retransmission]: {app_msg_str}")
            self.send_packet(packet, app_msg_str)

        sender_socket.close()
