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
print(f"Расстояние от 'me' до 'Tom': {distance}")