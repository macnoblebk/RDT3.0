from socket import *
from time import sleep

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