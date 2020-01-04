import queue
q=queue.PriorityQueue()
for i in range(5):
    q.put(i)

while not q.empty():
    print(q.get(),end=' ')
    print('\n')