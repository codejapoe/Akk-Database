class Char:
    def __init__(self, char, length=None, username=None, passcode=None):
        self.char = char
        self.length = Length(length, username, passcode)
        self.left = self.right = None

class Length:
    def __init__(self, length, username=None, passcode=None):
        self._id = length
        self.data = Data(username, passcode)
        self.left = self.right = None

class Data:
    def __init__(self, username, passcode):
        self.username = username
        self.passcode = passcode
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

def connect(root, node):
    if root is not None:
        connect(root.left, node)
        root.length = node
        connect(root.right, node)
    return root

if __name__ == "__main__":
    root = None
    charSet = ['n', 'g', 'd', 'k', 'b', 'e', 'i', 'l', 'a', 'c', 'f', 'h', 'j', 'm', 'u', 'r', 'x', 'p', 's', 'w', 'y', 'o', 'q', 't', 'v', 'z']
    for i in charSet:
        root = insertChar(root, i)

    node = None
    numberSet = [16, 8, 24, 4, 12, 20, 28, 2, 6, 10, 14, 18, 22, 26, 29, 1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 30]
    for j in numberSet:
        node = insertLength(node, j)

    root = connect(root, node)
