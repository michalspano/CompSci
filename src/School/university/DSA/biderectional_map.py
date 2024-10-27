#!/usr/bin/env python3

'''
Context: create an implementation of a Bidirectional Map.
Ensure that the invariants hold and the maps are bijective.
'''

from typing import Any

class BidirectionalMap:
    def __init__(self) -> None:
        # create initial empty HashMaps
        self.forward: dict  = {}
        self.backward: dict = {}


    def get(self, key) -> Any:
        try:
            key = str(key)
        except ValueError:
            print(f'{key} must be convertible to a string.')
        return self.forward[key]
       

    def reverse_get(self, value: str) -> Any:
        try:
            value = str(value)
        except ValueError:
            print(f'{value} must be convertible to a string.')
 
        return self.backward[value]
    
    '''
    To make the implementation more effective, we could directly
    try to access the values at the given keys, if an Exception
    is raised, we know that the key is not present in the map. So,
    we proceed with the algorithm accordingly.
    '''

    def put(self, key, value) -> None:
        if str(key) in self.forward:
            old_value: Any = self.forward[str(key)]
            del self.backward[str(old_value)]
        
        if str(value) in self.backward:
            old_key: Any = self.backward[str(value)]
            del self.forward[str(old_key)]
        
        # add or update removed values
        # the keys are always str, the values are some arbitrary type
        self.forward[str(key)]      = value
        self.backward[str(value)]   = key


    def get_forward(self) -> dict:
        return self.forward


    def get_backward(self) -> dict:
        return self.backward


if __name__ == '__main__':
    BiMap: BidirectionalMap = BidirectionalMap()

    BiMap.put(1, 'hello')
    BiMap.put(2, 'world')
    assert (res := BiMap.get(1)) == 'hello'; print(res)

    BiMap.put(3, 'hello')
    assert (res1 := BiMap.get_forward()) == {'3': 'hello', '2': 'world'}; print(res1)
    assert (res2 := BiMap.reverse_get('world')) == 2; print(res2)

    BiMap.put(2, 'space')
    assert (res3 := BiMap.get_forward()) == {'3': 'hello', '2': 'space'}; print(res3)
    assert (res4 := BiMap.get_backward()) == {'hello': 3, 'space': 2}; print(res4)

