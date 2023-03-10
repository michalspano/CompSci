#!/usr/bin/env python3

'''
Context: given a binary heap in the form of a list, we need to
check whether it is a valid min binary heap or not.
'''


def check(heap: list) -> bool:
    '''
    Check whether the given heap is a valid min binary heap or not.
    '''
    for i in range(len(heap)):
        left: int   = 2 * i + 1
        right: int  = 2 * i + 2

        if left < len(heap) and heap[i] > heap[left]:   return False
        if right < len(heap) and heap[i] > heap[right]: return False

    return True


if __name__ == '__main__':
    a: list = [1, 2, 3, 4, 5]               # true
    b: list = [100, 2, 3, 4, 5]             # false    
    c: list = [1, 1, 2, 10, 4, 5, 6, 7]     # false
    d: list = [2, 2, 2, 4, 5, 10, 12, 20]   # true

    assert (a_result := check(a));      print(f'isMinHeap({a}) = {a_result}')
    assert not (b_result := check(b));  print(f'isMinHeap({b}) = {b_result}')
    assert not (c_result := check(c));  print(f'isMinHeap({c}) = {c_result}')
    assert (d_result := check(d));      print(f'isMinHeap({d}) = {d_result}')

