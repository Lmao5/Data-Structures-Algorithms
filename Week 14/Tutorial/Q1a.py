import queue
myQueue = Queue()
for i in range( 16 ):
    if i % 3 == 0:
        myQueue.enqueue(i)
