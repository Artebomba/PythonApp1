from threading import *
import threading
from time import sleep

lock = threading.Lock()

class Example(Thread):
    def run(self):
        for i in range(5):
            lock.acquire()
            print("Hello from ExampleOne")
            sleep(1)
            lock.release()

class ExampleTwo(Thread):
    def run(self):
        for i in range(5):
            lock.acquire()
            print("Hello from ExampleTwo")
            sleep(1)
            lock.release()
            
example = Example()
exampleTwo = ExampleTwo()
example.start()
exampleTwo.start()
example.join()
exampleTwo.join()
print("End")