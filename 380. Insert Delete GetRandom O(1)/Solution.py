import random
class RandomizedSet:

    def __init__(self):
        self.S = set()
        self.v = []

    def insert(self, val: int) -> bool:
        if len(self.S) == 0 or val not in self.S:
            self.S.add(val)
            self.v.append(val)
            return True
        return False

    def remove(self, val: int) -> bool:
        if val in self.S:
            self.S.remove(val)
            self.v.remove(val)
            return True
        return False

    def getRandom(self) -> int:
        return random.choice(self.v)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
