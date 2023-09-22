from threading import Thread

class Cube:
    def __init__(self, width):
        self.width = width

    def volume(self):
        return self.width ** 3

    def perimeter(self):
        return self.width * 12

# Class Queue to manage gather the results of the Cube's methods
class Queue:
    def __init__(self):
        self.__resultList = []

    def add(self, element):
        self.__resultList.append(element)

    # reconfigure the string method for this class to print the result list
    def __str__(self):
        result = ''
        nr = 1
        for i in range(0, len(self.__resultList), 2):
            result += f'Perimeter for cube {nr} = {self.__resultList[i]}mm\n'
            result += f'Volume for cube {nr} = {self.__resultList[i]}mm2\n'
            nr += 1
        return result

# Class ThreadQueue - to put the Cube's methods in individual threads (using a list)
class ThreadQueue:
    def __init__(self):
        self.__threadList = []

    # Add all the methods for onea Cube oject to the queue
    def addth(self, object, resultsQueue):
        self.__threadList.append(Thread(target=lambda obj, que: que.add(
            obj.perimeter()), args=(object, resultsQueue))) # the perimeter calculation
        self.__threadList.append(Thread(target=lambda obj, que: que.add(
            obj.volume()), args=(object, resultsQueue))) # the volume calculation

    # Method to start all the threads in order
    def startThreads(self):
        for th in self.__threadList:
            th.start()

    # Method to stop the main thread and execute al the other threads in the list
    def joinThreads(self):
        for th in self.__threadList:
            th.join()
