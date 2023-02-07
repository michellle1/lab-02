"""
Server receiver buffer is char[256]
If correct, the server will send a message back to you saying "I got your message"
Write your socket client code here in python
Establish a socket connection -> send a short message -> get a message back -> ternimate
use python "input->" function, enter a line of a few letters, such as "abcd"
"""
import socket

def main():
    # TODO: Create a socket and connect it to the server at the designated IP and port
    HOST = "172.20.10.10" #server's hostname or IP address (use IP address of RPi when using rpi: 172.20.10.10) (localhost is used when just testing with your own device)
    PORT = 8000 #port used by the server (10000 or 8000 works)
    
    #with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    
    
    # TODO: Get user input and send it to the server using your TCP socket
    inp = input('Message:\n')
    b_inp= bytes(inp, 'utf-8') #convert string into bytes 
 
    s.sendall (b_inp)
    
    # TODO: Receive a response from the server and close the TCP connection
    
    data = s.recv(1024).decode() #socket is receiving data in a buffer size of 1024 bytes at a time #decode reverses the encryption from the server
    print(f"Received {data!r}")
    s.close()
    pass


if __name__ == '__main__':
    main()
