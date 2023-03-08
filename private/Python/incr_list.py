#!/usr/bin/env python3

'''
Based on an exam from DIT182 ~06/2022 of the course @ SEM | Chalmers.
This is a simple function that takes a list of integers from 0 to n (size k)
and check whether all the integers from 0 to n are present in the list. Duplicates
are allowed. The function returns True if all the integers are present and False
otherwise. The function should run at O(n + k) time.

The way to think about this: only the lists of the size k >= n will have all the
integers from 0 to n. If the list is to be regarded as true, it must contain a set
of all the integers from 0 to n. We want to optimize the time complexity, so we can
use an Array of size n to keep track of the present integers via Boolean flags.
'''

def check(n: int, xs: list[int]) -> bool:
    contains: list[bool] = []                   # O(1) 
    for _ in range(n): contains.append(False)   # O(n)
    
    counter: int = 0                            # O(1)      
    for x in xs:                                # O(k)          
        if not contains[x]:                     # O(1)       
            contains[x] = True                  # O(1)        
            counter += 1                        # O(1)  

    return counter == n                         # O(1)   


'''
Having O(n) + O(k) = O(n + k) time complexity - as desired! :)
The Set data structure would have been a better choice, but it would have
required O(log(n)) order of growth for the insertion and lookup operations.
'''


if __name__ == '__main__':
    # perform tests on some dummy data
    a: list = [1, 2, 10]
    b: list = [i for i in range(12)]
    c: list = [i for i in range(12)] + [1, 1, 2, 10]
    
    # check the results
    assert (a_result := check(12, a) == False); print(f'check(12, {a}) = {a_result}')
    assert (b_result := check(12, b) == True);  print(f'check(12, {b}) = {b_result}')
    assert (c_result := check(12, c) == True);  print(f'check(12, {c}) = {c_result}')

