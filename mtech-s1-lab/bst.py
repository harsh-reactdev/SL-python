class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None
    
    def insert(self, data):
        self.root = self._insert(self.root, data)
    
    def _insert(self, node, data):
        if not node:
            return Node(data)
        if data < node.data:
            node.left = self._insert(node.left, data)
        else:
            node.right = self._insert(node.right, data)
        return node
    
    def search(self, data):
        return self._search(self.root, data)
    
    def _search(self, node, data):
        if not node:
            return False
    
        if data == node.data:
            return True
        
        return self._search(node.left, data) if data < self.root.data else self._search(node.right, data)
    
    def display(self):
        self.in_order(self.root)
    
    def in_order(self, node = None):
        if node:
            self.in_order(node.left)
            print(node.data, end=' ')
            self.in_order(node.right)

if __name__ == '__main__':
    bst = BST()

    while True:
        print('\n1. Insert 2. Search 3. Display 4. Exit')
        choice = input('Enter your choice : ')
        match(choice):
            case '1':
                data = input('Enter the data to be inserted  : ')
                bst.insert(data)
            
            case '2':
                data = input('Enter the value to be searched : ')
                bst.search(data)
            
            case '3':
                bst.display()
            
            case '4':
                print('Exiting program...')
                break
        
            case _:
                print('Invalid choice, Try again.!')