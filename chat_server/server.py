import socket
import sys
from socket import SHUT_RDWR

### Important info on TCP - TIME_WAIT status:
'''

Running an example several times with too small delay between executions, could lead to this error:

socket.error: [Errno 98] Address already in use
This is because the previous execution has left the socket in a TIME_WAIT state, and can’t be immediately reused.

There is a socket flag to set, in order to prevent this, socket.SO_REUSEADDR:

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((HOST, PORT))

the "SO_REUSEADDR" flag tells the kernel to reuse a local socket in TIME_WAIT state, without waiting for its natural timeout to expire.

'''

# Create a Socket
def create_socket():
    try:
        global host
        global port
        global s
        global s2
        global port2
        host =""
        port =9998
        s= socket.socket()

    except socket.error as msg:
        print ("socket creation error: "+str(msg))

def create_send_socket():
    try:
        global host
        global port
        global s
        global s2
        global port2
        host =""
        port2 =9997
        s2= socket.socket()

    except socket.error as msg:
        print ("socket creation error: "+str(msg))

#Binding Socket and listening for connections
def bind_socket():
    try:
        global host
        global port
        global s
        global s2
        global port2
        print ("Binding the Port: "+str(port))

        s.bind((host,port))
        print ("Listening...")
        s.listen(5)
        
    except socket.error as msg:
        print ("socket creation error: "+str(msg) + "Retrying...")
        bind_socket()

def bind_send_socket():
    try:
        global host
        global port
        global s
        global s2
        global port2
        print ("Binding the Port2: "+str(port2))

        s2.bind((host,port2))
        print ("Next port Listening...")
        s2.listen(5)
        
    except socket.error as msg:
        print ("socket creation error: "+str(msg) + "Retrying...")
        bind_send_socket()

#Establish connection with a client (socket must be listening)

def socket_accept():
    conn,address = s.accept()
    print ("Connection has been established - IP: "+address[0]+" Port "+str(address[1]))
    print ("The above connection will be closed and new one will open. Host port "+str(port)+" will be used for listening!")
    conn.send(str.encode("9997"))
    conn.close()
    #s.shutdown(SHUT_RDWR) #To avoid time_wait for TCP! Not working as expected.
    s.close()
    bind_send_socket()
    conn,address = s2.accept()
    print ("Connection has been established - IP: "+address[0]+" Port "+str(address[1]))
    
    run_comm(conn)

    conn.close()

#Print values
def run_comm(conn):
    while True:
        # cmd = input()
        # if cmd == "quit":
        #     conn.close()
        #     s.close()
        #     sys.exit()
        # if len(str.encode(cmd))>0:
        #     conn.send(str.encode(cmd))
        try:
            client_response = str(conn.recv(1024),"utf-8")
            print("> "+client_response)
            conn.send(str.encode(" "))
        except:
            print("Connection closed by client!\n")
            #sys.exit()
            #To continously listen
            conn.close()
            s.close()
            sys.exit()
            #main()


def main():
    create_socket()
    create_send_socket() #for clarity
    bind_socket()
    #bind_send_socket() #for clarity
    socket_accept()

main()