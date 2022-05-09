from threading import *
from time import sleep
class Example(Thread):
    def run(self):
        for i in range(10):
            print("Hello from ExampleOne")
            sleep(1)

class ExampleTwo(Thread):
    def run(self):
        for i in range(10):
            print("Hello from ExampleTwo")
            sleep(1)
            
example = Example()
exampleTwo = ExampleTwo()
example.start()
sleep(0.1)
exampleTwo.start()
