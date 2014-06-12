#!/usr/bin/env python
# @author Tylor Snyder
# 
# QueueAnything is a Queue and a function decorator allowing any 
#   function to be queued
#

import Queue
import threading

q = Queue.Queue()
WORKERS=7

def queuedFunction(func):
    """
    Function decorator that places function in the queue
    """
    def inner(*args, **kwargs):
        q.put((func, args, kwargs))
    
    return inner
    
class AnyQueue(threading.Thread):
    """
    AnyQueue class that recieves a function from a queue and runs it
    """
    def __init__(self, queue):
        self.queue = queue
        threading.Thread.__init__(self)

    def run(self):
        while 1:
            try:
                (function, args, kwargs) = self.queue.get_nowait()
                function(*args, **kwargs)
            except:
                break

if __name__ == "__main__":
    
    import time
    import random
    @queuedFunction
    def waitlongprint(text):
        """
        Sample function for queue
        """
        print "waiting on %s" % text
        time.sleep(random.randint(1,10))
        print text

    waitlongprint("test1")
    waitlongprint("test2")
    waitlongprint("test3")
    waitlongprint("test4")
    waitlongprint("test5")
    waitlongprint("test6")
    waitlongprint("test7")
    waitlongprint("test8")
    waitlongprint("test9")
    waitlongprint("test0")
    for x in range(WORKERS):
        AnyQueue(q).start()


