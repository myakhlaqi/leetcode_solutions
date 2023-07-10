#
# @lc app=leetcode id=705 lang=python3
#
# [705] Design HashSet
#

# @lc code=start
class NextPrime:
    def next(n):
        flag= True
        if (n %2 == 0):
            i = n + 1
        else:
            i = n + 2
        while True:
            if(NextPrime.isPrime(i)):
                return i
            i += 2
    def isPrime(n):
        for i in range(2,n):
            if (n%i == 0):
                return False
        return True
        

class MyHashSet:
    
    def hash(self,key):
        
        return key % self.size

    def __init__(self):
        self.size= NextPrime.next(10 ** 6 +1)
        self.has_list= [-1] * self.size

    def add(self, key: int) -> None:
        self.has_list[hash(key)] = key
        #print("{} -> key: {}".format(key,hash(key)))
            
        

    def remove(self, key: int) -> None:
        self.has_list[hash(key)] = -1

    def contains(self, key: int) -> bool:
        if self.has_list[hash(key)] == key:
            return True
        else:
            return False
        
        
print([]*4)

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
# @lc code=end

