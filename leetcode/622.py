class MyCircularQueue:    
    
    def __init__(self, k: int):
        self.queue = [None] * k
        self.size = k
        self.rear = self.front = -1

    def enQueue(self, value: int) -> bool:        
        # if queue is full
        if ((self.rear + 1) % self.size == self.front):
            return False
        
        # queue is empty
        elif self.front == -1:
            self.front = 0
            self.rear = 0
            self.queue[self.rear] = value
            return True
        
        # add to next position of rear
        else:
            self.rear = (self.rear + 1) % self.size
            self.queue[self.rear] = value
            return True
        

    def deQueue(self) -> bool:        
        # queue is empty
        if self.front == -1:
            return False
        
        # queue has only 1 element
        elif self.front == self.rear:
            self.queue[self.front] = None
            self.front = -1
            self.rear = -1
            return True
        
        # remove front element
        else:
            self.queue[self.front] = None
            self.front = (self.front + 1) % self.size
            return True
        

    def Front(self) -> int:
        if self.front == -1:
            return -1
        else:
            return self.queue[self.front]
        

    def Rear(self) -> int:
        if self.rear == -1:
            return -1
        else:
            return self.queue[self.rear]
        

    def isEmpty(self) -> bool:
        return self.front == self.rear and self.front == -1

        
    def isFull(self) -> bool:
        return (self.rear + 1) % self.size == self.front


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()