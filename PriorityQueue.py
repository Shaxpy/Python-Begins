import queue

q=queue.PriorityQueue()
#using tuples
q.put((1,'prior 1'))
q.put((3,'prior 3'))
q.put((4,'prior 4'))
q.put((2,'prior 2'))
for i in range(q.qsize()):
    print(q.get()[1])