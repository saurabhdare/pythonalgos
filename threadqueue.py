import threading
import queue
import time

exitFlag = 0

class MyThread(threading.Thread):
    def __init__(self, threadID, name, q):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.q = q
    
    def run(self):
        print("Starting " + self.name)
        process_data(self.name, self.q)
        print("Exiting " + self.name)

def process_data(threadName, q):
    while not exitFlag:
        queueLock.acquire()
        if not workQueue.empty():
            data = q.get()
            queueLock.release()
            print("%s processing %s" % (threadName, data))
        else:
            queueLock.release()
            # seconds
            time.sleep(1)

# lists
threadList = ["Thread-1", "Thread-2", "Thread-3"]
nameList = ["One", "Two", "Three", "Four", "Five"]

# lock and queue
queueLock = threading.Lock()
workQueue = queue.Queue(10)

threads = []
threadID = 1

# create new threads
for tname in threadList:
    thread = MyThread(threadID, tname, workQueue)
    thread.start()
    threads.append(thread)
    threadID += 1

# fill the queue
queueLock.acquire()
for word in nameList:
    workQueue.put(word)

queueLock.release()

# wait for queue to empty
while not workQueue.empty():
    pass

# Notify threads it's time to exit
exitFlag = 1

# Wait for all threads to complete
for t in threads:
    t.join()

print("Exiting Main Thread")
