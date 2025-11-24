class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def hash_function(self, key):
        return hash(key) % self.size
    
    def insert_key(self, key, value):
        index = self.hash_function(key)
        for pair in self.table[index]:
            if pair[0] == key:
                pair[1] = value
                print(f'Updated {key} with new value {value}')
                return
            
        self.table[index].append([key, value])
        print(f'Inserted key {key}, value {value}')

    def search_key(self, key):
        index = self.hash_function(key)
        for pair in self.table[index]:
            if pair[0] == key:
                return pair[1]
        return None
    
    def display(self):
        for i, bucket in enumerate(self.table):
            print(f'Index {i} : {bucket}')