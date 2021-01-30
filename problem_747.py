from typing import List

# 747. Largest Number At Least Twice of Others
# https://leetcode.com/problems/largest-number-at-least-twice-of-others/

class Solution:

    def dominantIndex(self, nums: List[int]) -> int:
        '''
            Idea:
            Loop through the whole list and find the max and the next max
            Then just just compare max with the next max doubled
        '''
        max = nums[0]
        max_pos = 0
        max_next = 0

        for i in range(0, len(nums)):
            if nums[i] > max:
                max_next = max
                max = nums[i]
                max_pos = i
            elif nums[i] != max and nums[i] > max_next:
                max_next = nums[i]

        if max >= max_next * 2:
            return max_pos
        else:
            return -1

    def dominantIndex2(self, nums: List[int]) -> int:
        '''
            Idea:
            Sort list and compare last to the previous value doubled
            If ok, return the index of the last in the original list
            Runtime: 40 ms, faster than 28.77%
            Memory Usage: 14.3 MB, less than 12.09%
        '''
        if len(nums) == 1:
            return 0
        snums = sorted(nums)
        if snums[-1] >= snums[-2]*2:
            return nums.index(snums[-1])
        else:
            return -1


if __name__ == '__main__':
    s = Solution();
    assert s.dominantIndex([1]) == 0, "V1 Expected 0"
    assert s.dominantIndex([3, 6, 1, 0]) == 1, "V1 Expected 1"
    assert s.dominantIndex([0, 1, 6, 2]) == 2, "V1 Expected 2"
    assert s.dominantIndex([1, 2, 3, 4]) == -1, "V1 Expected -1"
    assert s.dominantIndex2([1]) == 0, "V2 Expected 0"
    assert s.dominantIndex2([3, 6, 1, 0]) == 1, "V2 Expected 1"
    assert s.dominantIndex2([0, 1, 6, 2]) == 2, "V2 Expected 2"
    assert s.dominantIndex2([1, 2, 3, 4]) == -1, "V2 Expected -1"
    print("Accepted")