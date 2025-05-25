import socket
import argparse
import sys
parser = argparse.ArgumentParser(description='Client centreon pour windows')
parser.add_argument("--hostname", help="adresse ip de la machine", required=True)
parser.add_argument("--password", help="mot de passe de l'agent", required=True)
parser.add_argument("--port", help="port de l'agent", required=True)
parser.add_argument("--warning", default=80, help="warning" )
parser.add_argument("--critical", default=90, help="critical")
args = parser.parse_args()
def client_program(param1,param2,param3,param4,param5):
    try:
        client_socket = socket.socket() 
        client_socket.connect((param1, int(param2)))
        client_socket.send(param3.encode())
        retour1 = client_socket.recv(1024).decode()
        if retour1 !="password_ok":
            client_socket.close()
            print ("CRITICAL -  password incorrect")
            sys.exit(2)
        client_socket.send("cpu_percent".encode()) 
        retour = client_socket.recv(1024).decode() 
        retour=float(retour)
        if  int(param4) <= int(retour) < int(param5):
            print('WARNING : CPU usage  ',retour,'% | cpu_usage%=',retour)
            sys.exit(1)
        elif  int(param5) <= int(retour):
            print('CRITICAL : CPU usage  ',retour,'% | cpu_usage%=',retour)
            sys.exit(2)    
        elif int(retour) < int(param4):
            print('OK : CPU usage  ',retour,'% | cpu_usage%=',retour)
            sys.exit(1)
        else:
            print('CRITICAL : sur le retour ')
            sys.exit(2)            
    except Exception as e:
        client_socket.close()
        print ("CRITICAL - probleme  :",e)
        sys.exit(2)
if __name__ == '__main__':
    client_program(args.hostname,args.port,args.password,args.warning,args.critical)