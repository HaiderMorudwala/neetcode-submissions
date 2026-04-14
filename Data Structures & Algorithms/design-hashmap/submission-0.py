class MyHashMap:

    def __init__(self):
        self.size = 1000
        self.map = [[] for _ in range(self.size)]

    def hash(self, key):
        return key % self.size

    def put(self, key, value):
        index = self.hash(key)
        bucket = self.map[index]

        for i in range(len(bucket)):
            if bucket[i][0] == key:
                bucket[i][1] = value   # update
                return
        
        bucket.append([key, value])   # insert

    def get(self, key):
        index = self.hash(key)
        bucket = self.map[index]

        for k, v in bucket:
            if k == key:
                return v
        
        return -1

    def remove(self, key):
        index = self.hash(key)
        bucket = self.map[index]

        for i in range(len(bucket)):
            if bucket[i][0] == key:
                bucket.pop(i)
                return