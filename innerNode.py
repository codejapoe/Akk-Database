class childNode:
    def __init__(self, _id, data):
        self._id = _id
        self.data = data
        self.left = self.right = None

def insert(node, _id, data):
    if node is None:
        return childNode(_id, data)

    oldId = node._id
    newId = _id

    if oldId > newId:
        node.left = insert(node.left, _id, data)
        return node

    elif oldId < newId:
        node.right = insert(node.right, _id, data)
        return node
    
    else:
        print("ID already exists...")
        return node

def inorder(node):
    if node is not None:
        inorder(node.left)
        print(f"ID: {node._id}, Data: {node.data}")
        inorder(node.right)

if __name__ == "__main__":
    root = None
    while True:
        _id:str = input("ID: ")
        data = input("Data: ")
        root = insert(root, _id, data)
        inorder(root)