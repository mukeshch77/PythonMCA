# Write a function to count and evaluate a = n * 10 for all values from 
import time

def count(n):
    for i in range(0,n):
        a = n * 10


ns = [1000000, 235346, 525253, 3423, 3223, 234234]

# # ------------------------------------------------------------------------------------
# # code to evalute run time of function call count(n)
# start_time = time.time() * 1000000
# # print(start_time)

# count(n) #timing this function call/execution
# end_time = time.time() * 1000000
# # print(end_time)


# print (f"\nTime to execute is {end_time - start_time} micro seconds")
# #---------------------------------------------------------------------------------------

def wrapper(func, n):
    # code to evalute run time of function call count(n)
    start_time = time.time() * 1000000
    # print(start_time)

    func(n)# timing this function call/execution

    end_time = time.time() * 1000000
    # print(end_time)

    print (f"\nTime to execute is {end_time - start_time} micro seconds")

for n in ns:
    wrapper(count, n)