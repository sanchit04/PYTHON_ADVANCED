# Sharing of data across threads is very easy since threads share same memory and space
# but we have to be very careful on the race condition
# Race condition happens when two or more threads tries to update same variable

import time
from threading import Thread,Lock

db_value=0
def increase():
    global db_value
    local_copy = db_value
    local_copy+=1
    time.sleep(0.1) # We are sleeping here
    db_value=local_copy # We are updating global db value

def increase_with_lock(lock):
    global db_value
    with lock:
        local_copy = db_value
        local_copy+=1
        time.sleep(0.1) # We are sleeping here
        db_value=local_copy # We are updating global db value

if __name__=="__main__":
    thread1 = Thread(target=increase)
    thread2 = Thread(target=increase)

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    print(f"FINAL DB VALUE:{db_value}")
    # WHY IS ABOVE VALUE 1 since there was a race condition between two threads
    # both the threads accesses the increase method at a same time thus both got initial value as 0
    # Ideally only thread1 should have got initial as 0
    # thread2 should have got initial as 1

    # TO FIX THIS RACE CONDITION WE NEED TO INTRODUCE LOCK
    lock = Lock()
    thread3 = Thread(target=increase_with_lock,args=(lock,))
    thread4 = Thread(target=increase_with_lock,args=(lock,))

    thread3.start()
    thread4.start()

    thread3.join()
    thread4.join()
    print(f"FINAL DB VALUE:{db_value}") # OP -> 3 as per expectation!