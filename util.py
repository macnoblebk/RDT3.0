def create_checksum(packet_wo_checksum):
    """create the checksum of the packet (MUST-HAVE DO-NOT-CHANGE)

    Args:
      packet_wo_checksum: the packet byte data (including headers except for checksum field)

    Returns:
      the checksum in bytes

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
    """verify packet checksum (MUST-HAVE DO-NOT-CHANGE)

    Args:
      packet: the whole (including original checksum) packet byte data

    Returns:
      True if the packet checksum is the same as specified in the checksum field
      False otherwise

    """
    checksum = packet[8:10]  # Extract checksum from the packet
    packet_wo_checksum = packet[:8] + packet[10:]
    return create_checksum(packet_wo_checksum) == checksum

def make_packet(data_str, ack_num, seq_num):
    """Make a packet (MUST-HAVE DO-NOT-CHANGE)

    Args:
      data_str: the string of the data (to be put in the Data area)
      ack: an int tells if this packet is an ACK packet (1: ack, 0: non ack)
      seq_num: an int tells the sequence number, i.e., 0 or 1

    Returns:
      a created packet in bytes

    """
    # make sure your packet follows the required format!
    header = b'COMPNETW'
    msg = data_str.encode()
    data_len = len(header + msg) + 4
    length_flags = (data_len << 2) | (ack_num << 1) | seq_num  # Insert ack and seq
    len_bytes = length_flags.to_bytes(2, byteorder='big')
    check_sum = create_checksum(header + msg + len_bytes)
    packet = header + check_sum + len_bytes + msg
    return packet


###### These three functions will be automatically tested while grading. ######
###### Hence, your implementation should NOT make any changes to         ######
###### the above function names and args list.                           ######
###### You can have other helper functions if needed.                    ######  


def extract_ack_seq(packet): return packet[11] & 0b1