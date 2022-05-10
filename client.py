import socket
import json

if __name__ == "__main__":

    while True:

            client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            client.connect(('localhost',80))
            print("Connected to server.")

            option = int(input("----------Akk Database----------\n 0. Exit\n 1. Create an account\n 2. Print Users\n 3. Search Data\n 4. Delete\n Your option: "))
            
            if option == 0:
                break

            elif option == 1:
                username = input("Username: ")

                if len(username) > 30:
                    print("No more than 30 characters...")
                    continue

                password = input("Password: ")
                data = {'option': 1, 'username': username, 'password': password}

            elif option == 2:
                data = {'option': 2}

            elif option == 3:
                username = input("Username: ")
                data = {'option': 3, 'username': username}

            elif option == 4:
                username = input("Username: ")
                data = {'option': 3, 'username': username}
        
            data = json.dumps(data)
            msg = bytes(data,'utf-8')
            client.send(msg)
            recvSMSMfromServer = client.recv(4096)
            print(f'[+] Received message from server: {recvSMSMfromServer.decode("utf-8")}')
            client.close()