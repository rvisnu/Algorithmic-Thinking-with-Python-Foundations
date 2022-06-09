import random

def binary_search(number, my_list):
    low = 0
    high = len(my_list)-1
    mid = 0

    while low<high:
        mid = (low + high)//2
        if my_list[mid] == number:
            return mid
        elif my_list[mid] > number:
            high = mid - 1
        else:
            low = mid + 1
    return -1

rand_list = [random.randint(1,100) for i in range(10)]
rand_list.append(45)
rand_list.sort()
print(rand_list)
print(binary_search(45, rand_list))

#https://www.cs.usfca.edu/~galles/visualization/Search.html