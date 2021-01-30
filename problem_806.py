from typing import List

# 806. Number of Lines To Write String
# https://leetcode.com/problems/number-of-lines-to-write-string/

class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        '''
            Idea:
            Loop through each character of s
            get the ASCII value of the character and subtract 97 (ascii of a)
            use this value to locate the pixels of the character in widths
            depending on the pixels update lines and line_pixels (current line pixels)
        '''
        lines = 1
        line_pixels = 0
        for ch in s:
            index = ord(ch) - 97
            w = widths[index]
            if line_pixels + w > 100:
                lines += 1
                line_pixels = w
            else:
                line_pixels += w
        return [lines, line_pixels]


if __name__ == '__main__':
    s = Solution();
    assert s.numberOfLines(
        [10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10],
        "abcdefghijklmnopqrstuvwxyz") == [3,60], "1. [3,60] expected"
    assert s.numberOfLines(
        [4, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],
        "bbbcccdddaaa") == [2, 4], "2. [2,4] expected"
    print("Accepted")