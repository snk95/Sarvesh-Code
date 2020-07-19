from collections import OrderedDict

class LRU_cache(OrderedDict):
    def __init__(self, capacity):
        self.capacity = capacity


    def put(self, key, value):
        if key in self:
            self.move_to_end(key)
        self[key] = value

        if len(self) > self.capacity:
            self.popitem(last=False)

    def get(self, key):
        if key not in self:
            return -1

        self.move_to_end(key)
        return self[key]

obj = LRU_cache(2)
obj.put(2,1)
obj.put(3,2)
print(obj.get(3))
print(obj.get(2))
obj.put(4,3)
print(obj.get(2))
print(obj.get(3))
print(obj.get(4))