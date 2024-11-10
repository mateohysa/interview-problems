'''
TWO-SUM using a hashmap and single pass through the array.

O(n) complexity
'''

class Solution(object):
    def twoSum(nums, target):
        checkedMap = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in checkedMap:
                return [checkedMap[diff], i]
            checkedMap[n] = i
        return

if __name__ == '__main__':
    print(Solution.twoSum([2, 7, 11, 15], 9))
