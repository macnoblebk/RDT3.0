# Project Title: 
## Reliable Transport Protocol 3.0 Implementation

### Description
Reliable Data Transfer 3.0, is a transport layer protocol implemented to ensure reliable and ordered delivery of data 
between sender and receiver despite potential errors, losses, or reordering of packets during transmission.

In this project, I implemented a reliable data transfer service using the stop-and-wait protocol (rdt3.0) capable of 
handling bit errors and packet loss. This project involved both sender and receiver implementations running at the 
application layer using UDP as the underlying transport service.


#### Differences between RDT and TCP  
- TCP is used in real-world networking scenarios.
- TCP has flow control
- TCP has congestion control
- TCP supports full-duplex communication
- TCP also supports multiplexing/demultiplexing with port numbers 

#### Differences between RDT and UDP 
- UDP is an unreliable transport service
- UDP  supports multiplexing/demultiplexing using port numbers 

#### Packet Format
![Packet format](Packet%20Format.png)

#### Finite State Machine - Receiver
![Receiver FSM](Receiver%20FSM.png)

#### Finite State Machine - Sender 
![Sender FSM](Sender%20FSM.png)

### Technologies and Skills
- Programming Languages: Python
- Libraries/Modules: Socket programming
- Concepts: Reliable data transfer, error detection, retransmission, acknowledgment, stop-and-wait protocol
- Tools: Command-line interface, debugging, Git

### Achievements and Contributions:
- Successfully implemented a reliable data transfer protocol that can handle common network issues such as bit 
errors and packet loss.
- Demonstrated ability to design and implement complex network protocols.
- Ensured reliability and efficiency in data transfer through error handling mechanisms.
- Enhanced problem-solving and debugging skills through rigorous testing and validation processes.

### Impact:
- Improved understanding of network protocols and error handling mechanisms.
- Developed a reusable and extendable codebase for future network-related projects.
- Provided a solid foundation for further enhancements, such as implementing more complex protocols or integrating 
additional security features.

### Future Enhancements:
- Transitioning from a stop-and-wait protocol to a pipelined protocol
- Adjustment of timeout management to handle multiple outstanding packets.
- Implementation of selective retransmission based on acknowledgment information.
- Introduction of a receiver window mechanism to regulate the flow of packets from the sender.
- Implementation of a congestion window mechanism to adjust the transmission rate based on network conditions.
- Enhancement of error detection and correction mechanisms to efficiently handle errors across multiple packets.