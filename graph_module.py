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

    def findMinNode(self, visited):
        min_val = None
        for cur_node in self.dict:
            if cur_node not in visited:
                if min_val is None:
                    min_val = cur_node
                elif min_val < 