import json
import socket

class Char:
    def __init__(self, char, length=None, username=None, password=None):
        self.char = char
        self.length = Length(length, username, password)
        self.left = self.right = None

class Length:
    def __init__(self, length, username=None, password=None):
        self._id = length
        self.data = Data(username, password)
        self.left = self.right = None

class Data:
    def __init__(self, username, password):
        self.username = username
        self.password = password
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

def insert(root, username, password):
    if username[0] == root.char:
        root.length = connectData(root.length, username, password)
        return root

    elif username[0] < root.char:
        root.left = insert(root.left, username, password)
        return root

    elif username[0] > root.char:
        root.right = insert(root.right, username, password)
        return root

def connectData(root, username, password):
    if len(username) == root._id:
        root.data = finalInsertion(root.data, username, password)
        return root

    elif len(username) < root._id:
        root.left = connectData(root.left, username, password)
        return root

    elif len(username) > root._id:
        root.right = connectData(root.right, username, password)
        return root

def finalInsertion(root, username, password):
    try:
        if root is None:
            root = Data(username, password)
            return root

        else:
            if username < root.username:
                root.left = finalInsertion(root.left, username, password)
                return root

            elif username > root.username:
                root.right = finalInsertion(root.right, username, password)
                return root

            elif username == root.username:
                print("Username already exists...")
                return root

    except:
        if root.username is None:
            root = Data(username, password)
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
            childData = {root.username: {'username': root.username, 'password': root.password}}
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
                data = {"username":username, "password":root.password}
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
                data = searchData(root.left, username)
                return data

            elif username > root.username:
                data = searchData(root.right, username)
                return data
            
            elif username == root.username:
                root.username = None
                root.password = None
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

if __name__ == "__main__":
    root = startDatabase()

    server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server.bind(('localhost', 80))
    server.listen(1)
    print("[*] Server started.")

    while True:
        client , address = server.accept()

        with client as sock:
            requestSMS = sock.recv(1024)
            requestSMS = requestSMS.decode("utf-8")

            if requestSMS != "":
                requestSMS = json.loads(requestSMS)
                option = requestSMS['option']

                if option == 1:                
                    root = insert(root, requestSMS['username'], requestSMS['password'])
                    sock.send(bytes('***Success***', 'utf-8'))

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
                        sock.send(bytes('***Success**', 'utf-8'))

                    else:
                        sock.send(bytes('No Data found...', 'utf-8'))