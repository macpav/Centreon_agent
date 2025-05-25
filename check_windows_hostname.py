import socket
import argparse
import sys
parser = argparse.ArgumentParser(description='Client centreon pour windows')
parser.add_argument("--hostname", help="adresse ip de la machine", required=True)
parser.add_argument("--password", help="mot de passe de l'agent", required=True)
parser.add_argument("--port", help="port de l'agent", required=True)
args = parser.parse_args()
def client_program(param1,param2,param3):
    try:
        client_socket = socket.socket() 
        client_socket.connect((param1, int(param2)))
        client_socket.send(param3.encode())
        retour1 = client_socket.recv(1024).decode()
        if retour1 !="password_ok":
            client_socket.close()
            print ("CRITICAL -  password incorrect")
            sys.exit(2)
        client_socket.send("hostname".encode()) 
        retour = client_socket.recv(1024).decode() 
        print('nom du serveur : ' + retour) 
        sys.exit(0)            
    except Exception as e:
        client_socket.close()
        print ("CRITICAL - probleme de connexion :",e)
        sys.exit(2)
if __name__ == '__main__':
    client_program(args.hostname,args.port,args.password)