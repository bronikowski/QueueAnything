#!/usr/bin/env python
import time
import random
import QueueAnything

@QueueAnything.queued
def waitprint(data):
    waittime = random.randint(1, 10)
    time.sleep(waittime)
    print "printed", data, "after", str(waittime), "seconds via waitprint()"


class ClassTest():

    @QueueAnything.queued
    def decorator_printit(self, data):
        waittime = random.randint(1, 10)
        time.sleep(waittime)
        print "printed", data, "after", str(waittime), "seconds via decorated_printit()"

    def printit(self, data):
        waittime = random.randint(1, 10)
        time.sleep(waittime)
        print "printed", data, "after", str(waittime), "seconds via printit()"


if __name__ == "__main__":
    waitprint("one")
    waitprint("two")
    waitprint("three")
    waitprint("four")

    x = ClassTest()
    x.decorator_printit("one")
    x.decorator_printit("two")
    x.decorator_printit("three")
    x.decorator_printit("four")

    x.printit = QueueAnything.queued(x.printit)
    x.printit("one")
    x.printit("two")
    x.printit("three")
    x.printit("four")

    QueueAnything.WORKERS = 12
    QueueAnything.start()
