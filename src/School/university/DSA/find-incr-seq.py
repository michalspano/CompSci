#!/usr/bin/env python3

'''
The exam of DIT182 from 2022/08 inspired to code this (of SEM @ GU|Chalmers).
It's a simple algorithm; it finds a list of integers which
is the maximal non-empty contiguous subsequence of increasing numbers.
'''


def find_runs(l: list) -> list[int]:
    runs: list[int] = []
    runs.append(0)

    for i in range(1, len(l)):
        if l[i - 1] >= l[i]:
            runs.append(i)

    return runs


if __name__ == '__main__':
    foo: list[int] = [42, 12, 54, 72, 36, 82, 99, 66, 6, 27]
    bar: list[int] = [42, 12, 12, 54, 54, 72, 36, 82, 99, 66, 6, 27]
    print(find_runs(foo)) 
    print(find_runs(bar))

