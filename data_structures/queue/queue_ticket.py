import time
import random

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

def line(until_show, max_time):
    person_que = Queue()
    sold_ticket = [] # チケットを買った人

    # 待ち人数100人を格納
    for i in range(100):
        person_que.push("person" + str(i))

    ticket_end = time.time() + until_show
    print(person_que.show())

    while time.time() < ticket_end and not person_que.is_empty():
        time.sleep(random.randint(0, max_time))
        sold_ticket.append(person_que.pop())
        print(sold_ticket)
    return sold_ticket
print(line(3, 1))