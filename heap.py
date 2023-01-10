import random


class MinHeap:
    def __init__(self):
        self.array = []
    def __init__(self,list):
        self.array = list
        self.heapify()
    def add(self, x):
        self.array.append( x )
        self.shift_up(len(self.array)-1)
    
    def update(self,index,new_value):
        old_value = self.array[index]
        self.array[index] = new_value
        if old_value < new_value:
            self.shift_down(index)
        else:
            self.shift_up(index)
    
    def shift_down(self,i):
        left = 2* i + 1
        right = 2* i + 2

        while (left < len(self.array) and self.array[left] < self.array[i]) or (
            right < len(self.array) and self.array[right] < self.array[i]
            ):
            smallest = left if right >= len(self.array) or self.array[left] < self.array[right] else right
            self.swap(smallest, i)
            i = smallest
            left = 2* i + 1
            right = 2* i + 2
                
    def shift_up(self,i):
        parent_ix = self.get_parent(i)
        while i != 0 and self.array[parent_ix] > self.array[i]:
            self.swap(i, parent_ix)
            i = parent_ix
            parent_ix = self.get_parent(i)
    
    def heapify(self):
        """
        We start at the last parent node and shift it down until the heap property is restored. 
        
        Then we move to the second to last parent node and shift it down until the heap property is
        restored. 
        
        We keep doing this until we move past the root node.
        """
        for i in range(len(self.array))[::-1]:
            self.shift_down(i)

    def get_parent(self,i):
        return i // 2 -1 if i % 2 == 0 else (i-1) // 2
        
    def swap(self, i, j):
        self.array[i], self.array[j] = self.array[j], self.array[i]
        
    def pop(self):
        if len(self.array) > 1:
            x = self.array[0]
            self.array[0] = self.array.pop()
            # save the min value at the free space at the end of heap for sorting if necessary
            # self.array[self.size-1] = x
            self.shift_down(0)
            return x
        elif len(self.array)==1:
            return self.array.pop()
        else:
            return -1
    def peek(self):
        return self.array[-1]

    def empty(self):
        return len(self.array) == 0

    def __str__(self) -> str:
        return str(self.array)
    def size(self):
        return len(self.array)

def heapsort(array):
    heap = MinHeap(array)
    return [heap.pop() for _ in range(heap.size()) ]


myheap = MinHeap([6,5,4,3,2,1])
print(heapsort([1,9,21,4,7,3,11,10,5,8,6]))
# for i in range(7)[::-1]:
#     # myheap.add(random.randint(1,10))
#     myheap.add(i)
print(myheap)
myheap.heapify()
print(myheap)
# myheap.pop()
# print(myheap)
# myheap.pop()
# print(myheap)
# myheap.add(1)
# print(myheap)
# myheap.update(1,0)
# print(myheap)

