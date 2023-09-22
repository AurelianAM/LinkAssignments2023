from cube2 import Cube, Queue, ThreadQueue

if __name__ == "__main__":

    cube1 = Cube(10)
    cube2 = Cube(20)

    # instantiate the queue for the results
    queue = Queue()
    # instantiate the queue for the threads
    threadQueue = ThreadQueue()

    # add the methods of the objects in the queue for the threads with individual thread for each method
    threadQueue.addth(cube1, queue)
    threadQueue.addth(cube2, queue)

    # start the threads form the queue
    threadQueue.startThreads()
    # stop the main thread and execute the threads from the queue
    threadQueue.joinThreads()

    # print the results - from the result's queue
    print(queue)