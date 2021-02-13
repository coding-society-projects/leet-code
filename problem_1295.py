from typing import List

# 1295. Find Numbers with Even Number of Digits
# https://leetcode.com/problems/find-numbers-with-even-number-of-digits/

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        '''
        Idea:
        Convert each number to string, check length-of-string mod 2 and
        if even, increase a counter
        '''
        counter = 0
        for num in nums:
            snum = str(num)
            if len(snum) % 2 == 0:
                counter += 1
        return counter


if __name__ == '__main__':
    s = Solution();
    assert s.findNumbers([12,345,2,6,7896]) == 2, "1. 2 expected"
    assert s.findNumbers([555,901,482,1771]) == 1, "2. 1 expected"
    print("Accepted")