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

def returnData(root):
    if root is not None:
        returnData(root.left)
        returnData2(root.length)
        returnData(root.right)

def returnData2(root):
    if root is not None:
        returnData2(root.left)
        returnData3(root.data)
        returnData2(root.right)

def returnData3(root):
    if root is not None:
        returnData3(root.left)
        if root.username is not None:
            print(f"Username: {root.username}, Password: {root.password}")
        returnData3(root.right)

if __name__ == "__main__":
    root = None
    charSet = ['n', 'g', 'd', 'k', 'b', 'e', 'i', 'l', 'a', 'c', 'f', 'h', 'j', 'm', 'u', 'r', 'x', 'p', 's', 'w', 'y', 'o', 'q', 't', 'v', 'z']

    for i in charSet:
        root = insertChar(root, i)

    root = connect(root)

    while True:

        try:
            username = input("Username: ")

            if len(username) > 30:
                print("No more than 30 characters...")
                continue

            password = input("Password: ")
            root = insert(root, username, password)
            returnData(root)

        except:
            print("Error occurred...")
            continue
