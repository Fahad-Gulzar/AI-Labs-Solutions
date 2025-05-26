# IMPLEMENT STACK USING PYTHON

class Stack:
    def _init_(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return "Stack is empty"

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return "Stack is empty"

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)


s = Stack()
s.push(10)
s.push(20)
s.push(30)
s.push(40)

print("Stack elements:", s.items)
print("Pop:", s.pop())
print("Peek:", s.peek())
print("Stack size:", s.size())


    # IMPLEMENT QUEUE USING PYTHON

class queue:
    def _init_(self):
        self.values = []

    def enqueue(self, x):
        self.values.append(x)

    def dequeue(self):
        front = self.values[0]
        self.values = self.values[1:]
        return front


q = queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
print(q.values)
print(q.dequeue())


    # IMPLEMENT BINARY SEARCH USING PYTHON


def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1


arr = [6, 12, 17, 23, 38, 45, 77, 84, 90]
target = 45

result = binary_search(arr, target)
if result != -1:
    print(f"Element {target} is present at index {result}")
else:
    print(f"Element {target} is not present in array")