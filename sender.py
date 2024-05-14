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

  ####### Your Sender class in sender.py MUST have the rdt_send(app_msg_str)  #######
  ####### function, which will be called by an application to                 #######
  ####### send a message. DO NOT change the function name.                    #######                    
  ####### You can have other functions if needed.                             #######   