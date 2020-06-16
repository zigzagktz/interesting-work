import time
import threading

amount=100

"""
both function will start working together and addressing the same global variable.
You can play around by changing the sleep time to see how things are changing.
For example, if I comment out the sleep time in subtraction function then the sub function
will perform and print the value and then after that the add function will worl.
But since both of them have some sleep time, they both show same output.
Also, important thing to notice is that the program run time is 2 second. 

"""

"""
Also, to prevent the collision of both the functions I am using lock such that
the resources are acquired by the function that has the lock.

As we can see the output, both threads have actually started at the same time,
but one of them performed the computation first before the another. 

"""

def add(num, locking):
    print(f'starting thread 1\n')
    locking.acquire()
    global amount
    time.sleep(2)
    amount = amount + num
    print(f'the amount is {amount} after addition...\n')
    locking.release()

def sub(num,locking):
    print(f'starting thread 2')
    locking.acquire()
    global amount
    amount = amount - num
    time.sleep(2)
    print(f'the amount is {amount} after subtraction\n')
    locking.release()


if __name__ == "__main__":

    start = time.time()

    locking= threading.Lock()

    a=10
    b=25

    t1 = threading.Thread(target=add, args=(a,locking))
    t2 = threading.Thread(target=sub, args=(b,locking))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    end =  time.time()
    
    print(f'total time to run is {end - start}')



"""
the output is

starting thread 1
starting thread 2

the amount is 110 after addition...

the amount is 85 after subtraction

total time to run is 4.094526052474976
"""
