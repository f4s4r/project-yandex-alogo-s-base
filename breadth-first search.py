from queue import Queue


class Graph:
    def __init__(self):
        self.dict = {}

    def add(self, key, value):
        if isinstance(value, list):
            self.dict[key] = value
        else:
            if key not in self.dict:
                self.dict[key] = []
            self.dict[key].append(value)

    def pop(self, key):
        if key in self.dict:
            return self.dict.pop(key)
        else:
            return None

    def show(self):
        for key, values in self.dict.items():
            for value in values:
                print(f"{key} --> {value}")
        print(self.dict)

    def getNeighbour(self, key) -> list:
        return self.dict.get(key, [])

    def BSF(self, start, target):
        queue = Queue()
        visited = set()
        queue.put((start, 0))
        visited.add(start)

        while not queue.empty():
            current_node, level = queue.get()

            if current_node == target:
                return level

            for neighbor in self.getNeighbour(current_node):
                if neighbor not in visited:
                    queue.put((neighbor, level + 1))
                    visited.add(neighbor)

        return -1
    

    def DSF(self, node, target, levels=0):

        if node == target:
            return levels
        
        neighbours = self.getNeighbour(node)
        for i in range(len(neighbours) if neighbours != '' else 0):
            res = self.DSF(neighbours[i], target, levels=levels + 1)
            if res is not None:
                return res


friends = Graph()
friends.add("me", ["Clair", "Alice", "Bob"])
friends.add("Bob", ["Paggi", "Anuge"])
friends.add("Clair", ["Tom", "Jonny"])
friends.add("Anuge", "")
friends.add("Alice", "Paggi")
friends.add("Paggi", "")
friends.add("Tom", "")
friends.add("Jonny", "")

distance = friends.BSF("me", "Tom")
#print(f"Расстояние от 'me' до 'Tom': {distance}")

numbers = Graph()
numbers.add('1', ['2', '7'])
numbers.add('2', ['3', '4'])
numbers.add('3', '')
numbers.add('4', ['5', '6'])
numbers.add('7', ['8', '9'])
numbers.add('8', '')
numbers.add('9', '')
distanceD = numbers.DSF('1', '9')
print(distanceD)