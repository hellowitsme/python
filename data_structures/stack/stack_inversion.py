class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)
    
    def show(self):
        return self.items

    def pop(self):
        return self.items.pop()
    
    def size(self):
        return len(self.items)

stack = Stack()
word = "Hello World!"
reverse_word = ""

for i in word:
    stack.push(i)

while stack.size():
    r = stack.pop()
    reverse_word += r

print(reverse_word)