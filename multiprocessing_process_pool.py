from multiprocessing import Pool

def cube(number):
    return number*number*number


if __name__ == "__main__":
    number_list = [1,2,3]
    pool = Pool()
    result=pool.map(cube,number_list) # can pass multiple elements
    result2=pool.apply(cube,[number_list[2]]) # Can pass only one single element at a time in an iter object
    pool.close()
    pool.join()
    print(result)
    print(result2)
    print("Reached to the END")