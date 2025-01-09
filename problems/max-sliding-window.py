import collections


class Solution(object):
    def maxSlidingWindow(self, nums, k):
        output = []
        window = collections.deque()
        left = right = 0

        while right < len(nums):
            while window and nums[window[-1]] < nums[right]:
                window.pop()  # pop element from deq if
            window.append(right)  # only indices to be kept in the deq

            if left > window[0]:
                window.popleft()

            if right + 1 >= k:
                output.append(nums[window[0]])
                left += 1
            right += 1
        return output

        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
