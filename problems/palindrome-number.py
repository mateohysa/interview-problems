'''
first reverse the number and just compare it to the original one
O(log(n))
'''

class Solution(object):
    def isPalindrome(self, x):
        ra = 0
        temp = x
        if x < 0:
            return False
        while (x > 0):
            ra = ra * 10 + x % 10
            x = x // 10
        return temp == ra
if __name__ == '__main__':
    print (Solution().isPalindrome(123));
    print(Solution().isPalindrome(121));