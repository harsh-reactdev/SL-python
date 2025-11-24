class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_node(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        
    def delete_node(self, data):
        if not self.head:
            print('list is empty.!')
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        current = self.head
        while current.next and current.next.data != data:
            current = current.next
        if current.next:
            current.next = current.next.next
        else:
            print('value not found in the list')
    
    def display(self):
        if not self.head:
            print('List is empty.!')
            return
        current = self.head
        while current:
            print(current.data, end=' --> ')
            current = current.next
        print('None')

if __name__ == '__main__':
    ll = LinkedList()

    while True:
        print('\n1. Add node 2. Delete node 3. Display Linked list 4. Exit')
        choice = input('Enter your choice : ')

        match(choice):
            case '1':
                data = input('Enter the value for the node : ')
                ll.insert_node(data)

            case '2':
                data = input('enter the value to be deleted : ')
                ll.delete_node(data)
            
            case '3':
                ll.display()

            case '4':
                print('Exiting program...')
                break
        
            case _:
                print('Invalid choice, Try again.!')
