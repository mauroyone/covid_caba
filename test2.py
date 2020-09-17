'''
Given an array of binary digits, sort the array so all 0s are at one end
and 1s in the other. Which end does not matter.
To sort the array swap any two adjacent elements.
Determine the minimum number of swaps to sort the array
'''

arr = [1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1]

def min_moves(array):
    number_of_ones = sum(array)
    number_of_zeros = len(array) - number_of_ones
    if number_of_zeros < number_of_ones:
        target = 0  #more 1s than 0s
    else:
        target = 1  #more 0s than 1s
    #more ones at the end, it's better to make an array [0, 0...1, 1]
    #if not, just invert the array
    if sum(array[:number_of_ones]) > sum(array[-number_of_ones:]):
        array = array[::-1]

    number_of_swaps = 0
    last_index = 0
    for i in range(number_of_zeros):
        index = array.index(target, last_index)
        last_index = index + 1
        number_of_swaps += index - i

    return number_of_swaps




print(min_moves(arr))
