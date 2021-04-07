# キューは最初に入れた要素が一番初めに取り出される(FIFO)
class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.insert(0, item)

    def pop(self):
        return self.items.pop()

    def show(self):
        return self.items

    def size(self):
        return len(self.items)

queue = Queue()
word = "Hello World!"
reverse = ""
for i in word:
    queue.push(i)
print(queue.show())
while queue.size():
    r = queue.pop()
    print(r)
    reverse += r

print(reverse)
print(queue.show())