from typing import List

class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        '''
        Idea:
        Use a list to store patterns found
        Convert each word to the respective morse code sequence.
        If sequence found is not in the patterns list, then add it
        Return the length of the patterns list (it will contain all unique patterns)
        '''
        patterns = []
        morse_code = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.",
                      "....", "..", ".---", "-.-", ".-..", "--", "-.",
                      "---", ".--.", "--.-", ".-.", "...", "-",
                      "..-", "...-", ".--", "-..-", "-.--", "--.."
                      ]
        for word in words:
            morse = ''
            for ch in word:
                morse += morse_code[ord(ch) - 97]
            if morse not in patterns:
                patterns.append(morse)

        return len(patterns)


if __name__ == '__main__':
    s = Solution();
    assert s.uniqueMorseRepresentations(["gin", "zen", "gig", "msg"]) == 2, "1. 2 expected"
    print("Accepted")
