import socket, threading

def connect(uname):
    while True:
        #submit button ke liye from se input lenna hai but right now we are taking input from stream 
        msg = input('\n')
        data = bytes(uname + '>' + msg,'utf-8')
        cli_sock.send(data)

def receive():
    while True:
        data = cli_sock.recv(1024)
        msg =  data.decode("utf-8") 
        print('\n'+ str(msg))

if __name__ == "__main__":   
    # socket
    cli_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # connect
    HOST = 'localhost'
    PORT = 5028

    uname = input('Enter your name to enter the chat > ')

    cli_sock.connect((HOST, PORT))     
    print('Connected to remote host...')


    thread_send = threading.Thread(target = connect,args=[uname])
    thread_send.start()

    thread_receive = threading.Thread(target = receive)
    thread_receive.start()