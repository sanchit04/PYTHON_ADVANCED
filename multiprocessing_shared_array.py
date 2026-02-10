from multiprocessing import Process, Lock, Array

def increase_element_counter(shared_num_array:Array,lock):
    with lock:
        num=0
        while num < len(shared_num_array[:]):
            shared_num_array[num]+=1
            num+=1

if __name__=="__main__":
    shared_array = Array('i',[1,2,3])
    lock = Lock()
    print(f"INITIAL SHARED ARRAY:{shared_array[:]}")
    # returns a printable list object
    # OP: INITIAL SHARED ARRAY:[1, 2, 3]
    p1=Process(target=increase_element_counter,args=(shared_array,lock))
    p2=Process(target=increase_element_counter,args=(shared_array,lock))

    p1.start()
    p2.start()

    p1.join()
    p2.join()
    print(f"FINAL SHARED ARRAY:{shared_array[:]}")
    # returns a printable list object
    # OP: FINAL SHARED ARRAY:[3, 4, 5]
    print("DONE PROCESSING")