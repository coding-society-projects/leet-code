# 1047. Remove All Adjacent Duplicates In String
# https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/

class Solution:
    """
    Idea:
    Iterate through the string and if a pair found, remove it and start over again
    from the beginning of the new string
    """
    def removeDuplicates(self, S: str) -> str:
        found = True
        while found:
            if len(S) <= 1:
                return S
            found = False
            for i in range(len(S)-1):
                if S[i] == S[i+1]:
                    S = S[:i] + S[i+2:]
                    found = True
                    break
        return S


if __name__ == '__main__':
    s = Solution();
    assert s.removeDuplicates("abbaca") == "ca", "1. ca expected"
    print("Accepted")