'''
Snail Sort

Given an n x n array, return the array elements arranged from outermost elements to the middle element, traveling clockwise.

array = [[1,2,3],
         [4,5,6],
         [7,8,9]]
snail(array) #=> [1,2,3,6,9,8,7,4,5]
'''
import numpy as np

def snail(snail_map):
    sm = np.array(snail_map)
    result = []
    while sm.shape > (0,0):
        for num in sm[0]:
            result.append(num)
        sm = np.delete(sm, 0, 0)
        sm = np.rot90(sm)
    return result