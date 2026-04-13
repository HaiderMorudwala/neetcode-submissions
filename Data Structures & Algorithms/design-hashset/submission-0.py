class MyHashSet:
    def __init__(self):
        self.size = 1000
        self.table = [[] for _ in range(self.size)]

    def _hash(self, key):
        return key % self.size

    def add(self, key: int) -> None:
        bucket_idx = self._hash(key)
        if key not in self.table[bucket_idx]:
            self.table[bucket_idx].append(key)

    def remove(self, key: int) -> None:
        bucket_idx = self._hash(key)
        if key in self.table[bucket_idx]:
            self.table[bucket_idx].remove(key)

    def contains(self, key: int) -> bool:
        bucket_idx = self._hash(key)
        return key in self.table[bucket_idx]