# QUEUES are thread safe FOLLOW FIFO First In First OUT

from queue import Queue

if __name__ =="__main__":
    q = Queue()
    q.put(1)
    q.put(2)
    q.put(3)

    print(q.get())# 1
    q.task_done()  # AFTER EVERY GET WE NEED TO DO TASK DONE OTHERWISE IT WILL KEEP ON RUNNING!
    print(q.get()) # 2
    q.task_done()
    print(q.get()) # 3
    q.task_done()
    print(q.get())  # theres nothing in queue it went into forver on mode
    q.task_done()
    # IT WENT INTO WAITING MODE WHERE ITS
    # WAITING FOR MORE elements MAIN THREAD IS RUNNING
    # q.get when queue is empty even after you do q.task_done will not stop the program!!
    q.join()
    print("END MAIN")