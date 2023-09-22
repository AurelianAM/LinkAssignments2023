import threading, logging

class Cube:
    def __init__(self, width):
        self.width = width
    
    def volume(self):
        vol = self.width ** 3
        print(f'Volume for {self.width}mm width cube is {vol}mm³')
    
    def perimeter(self):
        per = self.width * 12
        print(f'Perimeter of all edges for {self.width}mm width cube is {per}mm')

    #   this method is only for the second version of the main program
    #   implements the threading into the calculus method
    def calculus(self):
        t1 = threading.Thread(target=self.perimeter)
        t2 = threading.Thread(target=self.volume)
        t1.start()
        t2.start()
        t1.join()
        t2.join()

