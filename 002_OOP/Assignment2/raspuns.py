# Bună seara, 
# O variantă de realizare a clasei ar fi:

class Cube:
    def __init__(self, lat):
         self.lat = lat
    def calcul_volum(self):
        return self.lat ** 3
    def calcul_suma_laturi(self):
         return self.lat * 12 

# Crearea unui thread în acest caz ar putea să fie:
import threading
th_length = Thread(target=lambda cube, queue: queue.put(cube.calcul_suma_laturi()), args=(cube, resultsQueue)) 

# fiind utilizată o coadă pentru stocarea rezultatelor. 
resultsQueue = Queue()


# O variantă mai simplă de abordare ar putea să fie dată de următoarea clasă. 

class Cube:
     def __init__(self, side):
         self.side = side
     def cube_volume(self):
         logging.info("Volume of cube is: {}".format(self.side * self.side * self.side))
     def side_sum(self):
         logging.info("Sum of sides is: {}".format(self.side * 12)) 

# Trebuie observat că assignment-ul cere crearea a două obiecte de tip Cube, pentru fiecare din acestea, prin câte un fir, fiind executată o metodă. 

# În acest ultim caz, un exemplu de creare a unui fir ar putea 
ft1_1 = threading.Thread(target=cub1.side_sum()) 

# fiind creat desigur înainte obiectul:
cub1 = Cube(12) 