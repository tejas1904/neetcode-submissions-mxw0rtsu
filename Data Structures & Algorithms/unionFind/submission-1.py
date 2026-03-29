class UnionFind:
    
    def __init__(self, n: int):
        self.parent = {}
        for i in range(n):
            self.parent[i] = i
        

    def find(self, x: int) -> int:
        p = self.parent[x]
        while self.parent[p] != p:
            p = self.parent[p]
        return p

    def isSameComponent(self, x: int, y: int) -> bool:
        if self.find(x)==self.find(y):
            return True
        else:
            return False

    def union(self, x: int, y: int) -> bool:
        p1 = self.find(x)
        p2 = self.find(y)
        if p1==p2:
            return False

        self.parent[p2] = p1
        return True
        

    def getNumComponents(self) -> int:
        uniq_parents = set()
        for i in self.parent.keys():
            uniq_parents.add(self.find(i))
        return len(uniq_parents)

