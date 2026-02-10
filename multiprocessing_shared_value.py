# MULTIPROCESSING WITH SHARED Value
# provide a single value element

from multiprocessing import Process, Lock, Value

def increase_counter(shared_number:Value,lock:Lock):
    with lock:
        shared_number.value += 1
        print(f"Updated Counter:{shared_number.value}")

if __name__ =="__main__":
    lock=Lock()
    shared_number = Value('i',0)
    print(f"Initial value on main thread:{shared_number.value}")
    p1=Process(target=increase_counter,args=(shared_number,lock))
    p2=Process(target=increase_counter,args=(shared_number,lock))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print(f"Final value on main thread:{shared_number.value}")
