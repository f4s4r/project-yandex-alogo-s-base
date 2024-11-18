class Graph:
    def __init__(self):
        self.dict = {}
    

    def add(self, key, value):
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

        

graph1 = Graph()
graph1.add("1", "1.1")
graph1.add("1", "1.2")
graph1.add("2", "2.1")