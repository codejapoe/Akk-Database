import json
import socket

class Char:
    def __init__(self, char, length=None, username=None, password=None, amount=None):
        self.char = char
        self.length = Length(length, username, password, amount)
        self.left = self.right = None

class Length:
    def __init__(self, length, username=None, password=None, amount=None):
        self._id = length
        self.data = Data(username, password, amount)
        self.left = self.right = None

class Data:
    def __init__(self, username, password, amount):
        self.username = username
        self.password = password
        self.amount = amount
        self.left = self.right = None

def insertChar(node, char):
    if node is None:
        return Char(char)

    else:
        if char < node.char:
            node.left = insertChar(node.left, char)
            return node

        elif char > node.char:
            node.right = insertChar(node.right, char)
            return node

def insertLength(node, number):
    if node is None:
        return Length(number)

    else:
        if number < node._id:
            node.left = insertLength(node.left, number)
            return node

        elif number > node._id:
            node.right = insertLength(node.right, number)
            return node

def generate():
    node = None
    numberSet = [16, 8, 24, 4, 12, 20, 28, 2, 6, 10, 14, 18, 22, 26, 29, 1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 30]
    for j in numberSet:
        node = insertLength(node, j)
    return node

def connect(root):
    if root is not None:
        connect(root.left)
        node = generate()
        root.length = node
        connect(root.right)
    return root

def insert(root, username, password, amount):
    if username[0] == root.char:
        root.length = connectData(root.length, username, password, amount)
        return root

    elif username[0] < root.char:
        root.left = insert(root.left, username, password, amount)
        return root

    elif username[0] > root.char:
        root.right = insert(root.right, username, password, amount)
        return root

def connectData(root, username, password, amount):
    if len(username) == root._id:
        root.data = finalInsertion(root.data, username, password, amount)
        return root

    elif len(username) < root._id:
        root.left = connectData(root.left, username, password, amount)
        return root

    elif len(username) > root._id:
        root.right = connectData(root.right, username, password, amount)
        return root

def finalInsertion(root, username, password, amount):
    try:
        if root is None:
            root = Data(username, password, amount)
            return root

        else:
            if username < root.username:
                root.left = finalInsertion(root.left, username, password, amount)
                return root

            elif username > root.username:
                root.right = finalInsertion(root.right, username, password, amount)
                return root

            elif username == root.username:
                return root

    except:
        if root.username is None:
            root = Data(username, password, amount)
            return root

def returnData(root, data):
    if root is None:
        return data

    else:
        data = returnData(root.left, data)
        data = returnData2(root.length, data)
        data = returnData(root.right, data)
        return data

def returnData2(root, data):
    if root is None:
        return data
    
    else:
        data = returnData2(root.left, data)
        data = returnData3(root.data, data)
        data = returnData2(root.right, data)
        return data

def returnData3(root, data):
    if root is None:
        return data

    else:
        data = returnData3(root.left, data)
        if root.username is not None:
            childData = {root.username: {'username': root.username, 'password': root.password, 'amount': root.amount}}
            data.update(childData)
        data = returnData3(root.right, data)
        return data

def search(root, username):
    if username[0] == root.char:
        data = searchLength(root.length, username)
        return data

    elif username[0] < root.char:
        data = search(root.left, username)
        return data

    elif username[0] > root.char:
        data = search(root.right, username)
        return data

def searchLength(root, username):
    if len(username) == root._id:
        data = searchData(root.data, username)
        return data

    elif len(username) < root._id:
        data = searchLength(root.left, username)
        return data

    elif len(username) > root._id:
        data = searchLength(root.right, username)
        return data

def searchData(root, username):
    try:
        
        if root is None:
            return None

        else:
            if username < root.username:
                data = searchData(root.left, username)
                return data

            elif username > root.username:
                data = searchData(root.right, username)
                return data
            
            elif username == root.username:
                data = {"username": username, "password": root.password, "amount": root.amount}
                return data

            else:
                return None

    except:
        if root.username is None:
            return None

def delete(root, username):
    if username[0] == root.char:
        data = deleteLength(root.length, username)
        return data

    elif username[0] < root.char:
        data = delete(root.left, username)
        return data

    elif username[0] > root.char:
        data = delete(root.right, username)
        return data

def deleteLength(root, username):
    if len(username) == root._id:
        data = deleteData(root.data, username)
        return data

    elif len(username) < root._id:
        data = deleteLength(root.left, username)
        return data

    elif len(username) > root._id:
        data = deleteLength(root.right, username)
        return data

def deleteData(root, username):
    try:
        
        if root is None:
            return None

        else:
            if username < root.username:
                data = deleteData(root.left, username)
                return data

            elif username > root.username:
                data = deleteData(root.right, username)
                return data
            
            elif username == root.username:
                root.username = None
                root.password = None
                root.amount = None
                return True

            else:
                return None

    except:
        if root.username is None:
            return None

def startDatabase():
    root = None
    charSet = ['n', 'g', 'd', 'k', 'b', 'e', 'i', 'l', 'a', 'c', 'f', 'h', 'j', 'm', 'u', 'r', 'x', 'p', 's', 'w', 'y', 'o', 'q', 't', 'v', 'z']

    for i in charSet:
        root = insertChar(root, i)

    root = connect(root)
    return root


def update(root, username, data, option):
    if username[0] == root.char:
        data = updateLength(root.length, username, data, option)
        return data

    elif username[0] < root.char:
        data = update(root.left, username, data, option)
        return data

    elif username[0] > root.char:
        data = update(root.right, username, data, option)
        return data

def updateLength(root, username, data, option):
    if len(username) == root._id:
        data = updateData(root.data, username, data, option)
        return data

    elif len(username) < root._id:
        data = updateLength(root.left, username, data, option)
        return data

    elif len(username) > root._id:
        data = updateLength(root.right, username, data, option)
        return data

def updateData(root, username, data, option):
    try:
        
        if root is None:
            return None

        else:
            if username < root.username:
                data = updateData(root.left, username, data, option)
                return data

            elif username > root.username:
                data = updateData(root.right, username, data, option)
                return data
            
            elif username == root.username:

                if option == 1:
                    root.password = data

                elif option == 2:
                    root.amount = data

                return True

            else:
                return None

    except:
        if root.username is None:
            return None

if __name__ == "__main__":
    root = startDatabase()

    server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server.bind(('localhost', 80))
    server.listen(1)
    print("[*] Server started.")

    while True:

        try:
            client , address = server.accept()

            with client as sock:
                requestSMS = sock.recv(1024)
                requestSMS = requestSMS.decode("utf-8")

                if requestSMS != "":
                    requestSMS = json.loads(requestSMS)
                    option = requestSMS['option']

                    if option == 1:
                        root = insert(root, requestSMS['username'], requestSMS['password'], requestSMS['amount'])
                        sock.send(bytes('[*] Success', 'utf-8'))

                    elif option == 2:
                        data = returnData(root, {})
                        msg = json.dumps(data)
                        sock.send(bytes(msg, 'utf-8'))

                    elif option == 3:
                        data = search(root, requestSMS['username'])
                        msg = json.dumps(data)
                        sock.send(bytes(msg, 'utf-8'))

                    elif option == 4: 
                        result = delete(root, requestSMS['username'])

                        if result == True:
                            sock.send(bytes('[*] Success', 'utf-8'))

                        else:
                            sock.send(bytes('No Data found...', 'utf-8'))

                    elif option == 5:
                        result = update(root, requestSMS['username'], requestSMS['password'], 1)

                        if result == True:
                            sock.send(bytes('[*] Success', 'utf-8'))

                        else:
                            sock.send(bytes('No Data found...', 'utf-8'))

                    elif option == 6:
                        result = update(root, requestSMS['username'], requestSMS['amount'], 2)

                        if result == True:
                            sock.send(bytes('[*] Success', 'utf-8'))

                        else:
                            sock.send(bytes('No Data found...', 'utf-8'))

                    elif option == 7:
                        data = search(root, requestSMS['username'])

                        if data is None:
                            sock.send(bytes('[*] Username does not exist.', 'utf-8'))

                        else:
                            password = data['password']
                            amount = data['amount']
                            delete(root, requestSMS['username'])
                            root = insert(root, requestSMS['new_username'], password, amount)
                            sock.send(bytes('[*] Success', 'utf-8'))

                    elif option == 8:
                        data = search(root, requestSMS['username'])

                        if data is None:
                            sock.send(bytes('[*] Username does not exist.', 'utf-8'))

                        else:
                            amount = int(data['amount']) + int(requestSMS['amount'])

                        update(root, requestSMS['username'], amount, 2)
                        sock.send(bytes('[*] Success', 'utf-8'))

                    elif option == 9:
                        data = search(root, requestSMS['username'])

                        if data is None:
                            sock.send(bytes('[*] Username does not exist.', 'utf-8'))

                        else:
                            data2 = search(root, requestSMS['receiver'])

                            if data2 is None:
                                sock.send(bytes('[*] Username does not exist.', 'utf-8'))

                            else:
                                amount1 = int(data['amount']) - int(requestSMS['amount'])
                                update(root, requestSMS['username'], amount1, 2)

                                amount2 = int(data2['amount']) + int(requestSMS['amount'])
                                update(root, requestSMS['receiver'], amount2, 2)
                                sock.send(bytes('[*] Success', 'utf-8'))

        except:
            print('[*] Server Error')
            continue