class Solution:
    @staticmethod
    def is_palindrome(word: str):
        head = 0
        tail = len(word) - 1

        while head < tail:
            if word[head] != word[tail]:
                return False
            else:
                head += 1
                tail -= 1
        
        return True

    def longestPalindrome(self, s: str) -> str:
        word_length = len(s)

        for length in range(word_length, 0, -1):
            for start_idx in range(0, word_length - length + 1):
                subset = s[start_idx: start_idx + length]
                
                if Solution.is_palindrome(subset):
                    return subset
