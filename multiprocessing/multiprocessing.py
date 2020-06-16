import time
import multiprocessing
import sys




def add(amount, balance):
    print(f'adding {amount} in account')
    time.sleep(10)
    balance.value = balance.value + amount
    print("")

def sub(amount, balance):
    print(f'subtracting {amount} in account')
    time.sleep(10)
    balance.value = balance.value-amount
    print('subtraction is done')

if __name__ == "__main__":

    balance = multiprocessing.Value('i',200)
    start  = time.perf_counter()
    
    add_amount = 10
    sub_amount = 10
    
    p1 = multiprocessing.Process(target= add, args= (add_amount,balance))
    p2 = multiprocessing.Process(target= sub, args=(sub_amount,balance))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    end =  time.perf_counter()
    print(balance.value)
    print(f'time to run is {end-start} second ')
    
    
    
