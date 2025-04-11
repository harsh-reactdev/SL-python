from collections import defaultdict, deque

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def bfs(self, start):
        visited = set()
        queue = deque([start])

        print('BFS Traversal : ', end=' ')

        while queue:
            node = queue.popleft()
            if node not in visited:
                print(node, end=' ')
                visited.add(node)
                queue.extend(self.graph[node])
    
    def dfs(self, start, visited = None):
        if visited is None:
            visited = set()

        print(start, end=' ')
        visited.add(start)

        for neighbor in self.graph[start]:
            if neighbor not in visited:
                self.dfs(neighbor, visited)

if __name__ == '__main__':
    g = Graph()

    while True:
        print('\n1. Insert 2. BFS 3. DFS 4. Exit')
        choice = input('Enter your choice : ')
        match(choice):
            case '1':
                u = input('Enter the source node : ')
                v = input('Enter the destination node : ')
                g.add_edge(u, v)
            
            case '2':
                start = input('Enter the value for start node : ')
                g.bfs(start)
            
            case '3':
                start = input('Enter the value for start node : ')
                g.dfs(start)
            
            case '4':
                print('Exiting program...')
                break
        
            case _:
                print('Invalid choice, Try again.!')