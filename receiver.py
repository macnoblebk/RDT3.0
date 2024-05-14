from socket import *
from time import sleep
from util import *

BUFFER_SIZE = 1024
ADDRESS = ('', 10185)
SLEEP_DURATION = 5
TIMEOUT_FREQUENCY = 6
PACKET_CORRUPTION_FREQUENCY = 3
class Receiver:
    def __init__(self):
        self.receiver_socket = socket(AF_INET, SOCK_DGRAM)
        self.receiver_socket.bind(ADDRESS)
        self.previous_seq_num = -1
        self.packet_counter = 0

    def rdt_receive(self):
        while True:
            packet, sender_socket = self.receiver_socket.recvfrom(BUFFER_SIZE)
            self.packet_counter += 1
            print(f"\npacket num.{self.packet_counter} received: {packet}")

            valid_packet = verify_checksum(packet)

            if self.packet_counter % TIMEOUT_FREQUENCY == 0:
                print("simulating packet loss: sleep a while to trigger timeout event on the sender side...")
                sleep(SLEEP_DURATION)

            elif self.packet_counter % PACKET_CORRUPTION_FREQUENCY == 0 or not valid_packet:
                print("simulating packet bit errors/corrupted: ACK the previous packet")
                response_packet = make_packet('', 1, self.previous_seq_num)
                self.receiver_socket.sendto(response_packet, sender_socket)

            else:
                msg_str = packet[12:].decode('utf-8')
                print(f"packet is expected, message string delivered: {msg_str}")
                print("packed is delivered, now creating and sending the ACK packet...")
                seq_num = extract_ack_seq(packet)
                response_packet = make_packet('', 1, seq_num)
                self.previous_seq_num = seq_num
                self.receiver_socket.sendto(response_packet, sender_socket)

            print("all done for this packet!\n")
