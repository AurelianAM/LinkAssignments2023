from cube import Cube   # import Cube class
import threading        # import threading module

first_cube = Cube(20)   # created first object
second_cube = Cube(30)  # created second object

# if the main program has started
if __name__ == "__main__":
    # begin the first version of the program
    print("First variant of pthe program...")

    # define the threads for the first object's methods
    t1 = threading.Thread(target=first_cube.perimeter)
    t2 = threading.Thread(target=first_cube.volume)

    # define the threads for the second object's methods
    t3 = threading.Thread(target=second_cube.perimeter)
    t4 = threading.Thread(target=second_cube.volume)

    # start the first object's methods threads
    t1.start()
    t2.start()
    # start the second object's methods threads
    t3.start()
    t4.start()

    # execute the first object's methods threads
    t1.join()
    t2.join()
    # execute the first object's methods threads
    t3.join()
    t4.join()

    #  begin the second version of the program
    print("\nSecond variant of the program...")
    first_cube.calculus()
    second_cube.calculus()

print('\nProgram ended sucessfully!')