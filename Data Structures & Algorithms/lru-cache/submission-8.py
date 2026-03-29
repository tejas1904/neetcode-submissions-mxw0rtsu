class Node:
    def __init__(self,key,val,left=None,right=None):
        self.key = key
        self.val = val
        self.left = left
        self.right = right
class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity

        self.dicta = {}

        self.start = Node(None,None)
        self.end = Node(None,None)
        self.start.right = self.end
        self.end.left = self.start

    def removeNode(self,node):
        node.left.right = node.right
        node.right.left = node.left
    def insertBegining(self,node):
        node.right = self.start.right
        node.left = self.start

        self.start.right.left = node
        self.start.right = node
    def insertEnd(self,node):
        node.right = self.end
        node.left = self.end.left
        
        self.end.left.right = node
        self.end.left = node


    def get(self, key: int) -> int:
        if key in self.dicta:
            node = self.dicta[key]
            val = self.dicta[key].val
            self.removeNode(node)
            self.insertBegining(node)
            return val
        else:
            return -1
        
    def put(self, key: int, value: int) -> None:
        if key in self.dicta:
            node = self.dicta[key]
            node.val = value
            self.removeNode(node)
            self.insertBegining(node)
            
        elif len(self.dicta)<self.capacity:
            newnode = Node(key,value)
            self.insertBegining(newnode)
            self.dicta[key] = newnode
        else:
            lru_node = self.end.left
            self.removeNode(lru_node)
            self.dicta.pop(lru_node.key)
            
            newnode = Node(key,value)
            self.insertBegining(newnode)
            self.dicta[key] = newnode


        
