import socket, threading
import pickle
def accept_client():
    while True:
        #accept    
        cli_sock, cli_add = ser_sock.accept()
        #print(cli_sock)
        if cli_sock not in CONNECTION_LIST:
            CONNECTION_LIST.append(cli_sock)
        size_user_list = len(CONNECTION_LIST)
        if size_user_list%2==0 and size_user_list!=0 :
            print('*******************')
            ran_no = 1
            connection_dict[CONNECTION_LIST[size_user_list-1]] = CONNECTION_LIST[size_user_list-2]
            connection_dict[CONNECTION_LIST[size_user_list-2]] = CONNECTION_LIST[size_user_list-1]
        thread_client = threading.Thread(target = connect_usr, args=[cli_sock])
        thread_client.start()

def connect_usr(cli_sock):
    while True:
        try:
            data = cli_sock.recv(1024)
            if data:
               b_usr(cli_sock, data)
        except Exception as x:
            print(x.message)
            break

def b_usr(cs_sock, msg):
    au = connection_dict[cs_sock]
    au.send(msg)
    #for client in CONNECTION_LIST:
    #    if client != cs_sock:
    #        client.send(msg)
    #size = len(CONNECTION_LIST)
    #if size%2 == 0 :    
    #else:
        
        
if __name__ == "__main__":    
    CONNECTION_LIST = []
    connection_dict = {}
    problem = open('Problem.pickle','rb')
    problem_list = pickle.load(problem)
    problem.close()
    # socket
    ser_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # bind
    HOST = 'localhost'
    PORT = 5028
    ser_sock.bind((HOST, PORT))

    # listen    
    ser_sock.listen(5)
    print('Chat server started on port : ' + str(PORT))

    thread_ac = threading.Thread(target = accept_client)
    thread_ac.start()
