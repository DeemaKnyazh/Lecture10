from threading import Thread

class MyThread(Thread):
    """A thread that prints its name"""
    def __init__(self, name):
        Thread.__init__(self, name = name)

    def run(self):
        print("Hello, my name is %s" % self.name)

def main():
    MyThread("Jim").start()

if __name__ == "__main__":
    main()