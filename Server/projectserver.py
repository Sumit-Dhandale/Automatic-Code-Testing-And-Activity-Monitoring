import socket
import sys
import mysql.connector
import tester



######   Create a Socket ( connect two computers)  ######

def create_socket():
    try:
        global host
        global port
        global s
        host = ""
        port = 60001
        s = socket.socket()

    except socket.error as msg:
        print("Socket creation error: " + str(msg))




######   Binding the socket and listening for connections    ######
        
def bind_socket():
    try:
        global host
        global port
        global s
        print("Binding the Port: " + str(port))

        s.bind((host, port))
        s.listen(5)

    except socket.error as msg:
        print("Socket Binding error" + str(msg) + "\n" + "Retrying...")
        bind_socket()





######    Establish connection with a client (socket must be listening)    #######

def socket_accept():
    global conn
    conn, address = s.accept()
    print("Connection has been established! |" + " IP " + address[0] )
    #send_commands(conn)
    #conn.close()

#==============close the connection=============================#
def Close():
    x="CLOSE"
    send_commands(conn,x)
    conn.close()


######    Send commands to client     ########    

def send_commands(conn,x):
    conn.send(str.encode(x))

'''
def send_commands(conn):
    while True:
        cmd = input()
        if cmd == 'quit':
            conn.close()
            s.close()
            sys.exit()
        if len(str.encode(cmd)) > 0:
            conn.send(str.encode(cmd))
            if cmd == 'scr':
                for_scr()
            if cmd=='assign':
                assignment()
            if cmd=='reg':
                reg()
    return
'''

def for_scr():
    x="scr"
    send_commands(conn,x)
    file=open('screenshot.png','wb')
    m=conn.recv(128)
    data=m
    while True:
        m= conn.recv(128)
        data=data+m;
        if len(m)<128:
            break;
    file.write(data)





def assignment():
    x="assign"
    send_commands(conn,x)
    file1=open('assignment.py','wb')
    print('file opened successfully')
    n=conn.recv(128)
    data1=n
    #print(data1)
    while True:
        n=conn.recv(128)
        data1=data1+n
        #print("\nCHUNK written")
        if len(n)<128:
            break;
    file1.write(data1)
    file1.close()

    return tester.main('assignment.py')


def addtodatabase():
    mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='',
    database='mydatabase'
    )
    mycursor=mydb.cursor()
    file1=open('a.txt','r')
    buff=file1.read()
    mycursor.execute("")


def main():
    print("connecting....... ")
    create_socket()
    bind_socket()
    socket_accept()
    


main()

