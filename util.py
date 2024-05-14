def create_checksum(packet_wo_checksum):
    """
        Creates the checksum of the packet.
        Args:
            packet_wo_checksum (bytes): The packet byte data (including headers except for checksum field).
        Returns:
        bytes: The checksum in bytes.
    """
    checksum = 0
    # Sum 16-bit words
    for i in range(0, len(packet_wo_checksum), 2):
        if i + 1 < len(packet_wo_checksum):
            checksum += (packet_wo_checksum[i] << 8) + packet_wo_checksum[i + 1]

    # Fold the carry
    while checksum >> 16:
        checksum = (checksum & 0xffff) + (checksum >> 16)

    # Take one's complement
    checksum = ~checksum & 0xffff

    # Convert checksum to two bytes
    return bytes([(checksum >> 8) & 0xFF, checksum & 0xFF])

def verify_checksum(packet):
    """
        Verifies the packet checksum.
        Args:
            packet (bytes): The whole packet byte data (including original checksum).
        Returns:
            bool: True if the packet checksum is the same as specified in the checksum field, False otherwise.
    """
    checksum = packet[8:10]  # Extract checksum from the packet
    packet_wo_checksum = packet[:8] + packet[10:]
    return create_checksum(packet_wo_checksum) == checksum

def make_packet(data_str, ack_num, seq_num):
    """
        Creates a packet.
        Args:
            data_str (str): The string of the data (to be put in the Data area).
            ack_num (int): Indicates if this packet is an ACK packet (1: ack, 0: non ack).
            seq_num (int): The sequence number, i.e., 0 or 1.
        Returns:
            bytes: A created packet in bytes.
    """
    header = b'COMPNETW'
    msg = data_str.encode()
    data_len = len(header + msg) + 4
    length_flags = (data_len << 2) | (ack_num << 1) | seq_num  # Insert ack and seq
    len_bytes = length_flags.to_bytes(2, byteorder='big')
    check_sum = create_checksum(header + msg + len_bytes)
    packet = header + check_sum + len_bytes + msg
    return packet


def extract_ack_seq(packet):
    """
        Extracts the ACK sequence number from the packet.
        Args:
           packet (bytes): The packet byte data.
       Returns:
           int: The sequence number.
    """
    return packet[11] & 0b1