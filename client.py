import socket
import json

if __name__ == "__main__":

    while True:

        try:
            client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            client.connect(('localhost',80))

            option = int(input("----------Akk Database----------\n 0. Exit\n 1. Create an account\n 2. Print Users\n 3. Search Data\n 4. Delete\n 5. Update Password\n 6. Update Amount\n 7. Update Username\n 8. Withdraw Amount\n 9. Transfer money\n Your option: "))
            
            if option == 0:
                break

            elif option == 1:
                username = input("Username: ")

                if len(username) > 30:
                    print("No more than 30 characters...")
                    continue

                password = input("Password: ")
                amount = int(input("Amount: "))
                data = {'option': 1, 'username': username, 'password': password, 'amount': amount}

            elif option == 2:
                data = {'option': 2}

            elif option == 3:
                username = input("Username: ")
                data = {'option': 3, 'username': username}

            elif option == 4:
                username = input("Username: ")
                data = {'option': 4, 'username': username}

            elif option == 5:
                username = input("Username: ")
                password = input("Password: ")
                data = {'option': 5, 'username': username, 'password': password}

            elif option == 6:
                username = input("Username: ")
                amount = input("Amount: ")
                data = {'option': 6, 'username': username, 'amount': amount}

            elif option == 7:
                username = input("Old Username: ")
                new_username = input("New Username: ")
                data = {'option': 7, 'username': username, 'new_username': new_username}

            elif option == 8:
                username = input("Username: ")
                amount = input("Amount: ")
                data = {'option': 8, 'username': username, 'amount': amount}

            elif option == 9:
                username = input("Your username: ")
                receiver = input("Receiver's username: ")
                amount = input("Amount: ")
                data = {'option': 9, 'username': username, 'receiver': receiver, 'amount': amount}
        
            data = json.dumps(data)
            msg = bytes(data,'utf-8')
            client.send(msg)
            recv = client.recv(4096)
            print(f'[+] Received message from server: {recv.decode("utf-8")}')
            client.close()

        except:
            print('[*] Client Error.')
            continue