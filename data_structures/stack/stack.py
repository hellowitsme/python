# スタックは要素の追加や削除を終端にしかできない(LIFO)
class Stack:
    def __init__(self):
        self.items = []

    # スタックが空の時はTrue、そうで無いときはFalse
    def is_empty(self):
        return self.items == []

    # 要素をスタックに追加
    def push(self, item):
        self.items.append(item)

    # スタックの一番上の要素を削除して返す
    def pop(self):
        return self.items.pop()
    
    # スタックの一番上の要素を返す。削除はされない
    def peek(self):
        last = len(self.items) - 1
        return self.items[last]

    # スタックの要素数を返す
    def size(self):
        return len(self.items)

    def show(self):
        return self.items

stack = Stack()
word = "Hello World!"
for i in word:
    stack.push(i)
    print(stack.show())
    
print(stack.peek())
print(stack.size())