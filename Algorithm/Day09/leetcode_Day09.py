class MyHashMap1:

    def __init__(self):
        self.Map = dict()

    def put(self, key: int, value: int) -> None:
        if self.Map.get(key) :
            self.Map.pop(key)
        self.Map.setdefault(key, value)

    def get(self, key: int) -> int:
        result = self.Map.get(key)
        if result != None : return result
        else : return -1

    def remove(self, key: int) -> None:
        if self.Map.get(key):
            self.Map.pop(key)
        

class MyHashMap2:
    def __init__(self):
        self.map = [-1] * 1000001  # 최대 key 범위만큼 배열 확보

    def put(self, key: int, value: int) -> None:
        self.map[key] = value

    def get(self, key: int) -> int:
        return self.map[key]

    def remove(self, key: int) -> None:
        self.map[key] = -1

        

class MyHashMap3:
    def __init__(self):
        self.size = 1000
        self.buckets = [[] for _ in range(self.size)]

    def _hash(self, key):
        return key % self.size

    def put(self, key: int, value: int) -> None:
        h = self._hash(key)
        for pair in self.buckets[h]:
            if pair[0] == key:
                pair[1] = value
                return
        self.buckets[h].append([key, value])

    def get(self, key: int) -> int:
        h = self._hash(key)
        for pair in self.buckets[h]:
            if pair[0] == key:
                return pair[1]
        return -1

    def remove(self, key: int) -> None:
        h = self._hash(key)
        self.buckets[h] = [pair for pair in self.buckets[h] if pair[0] != key]
