class Solution(object):
    def isPalindrome(self, s):
        s = "".join(ch.lower() for ch in s if ch.isalnum())
        head = 0
        tail = len(s) - 1

        while head <= tail:
            if s[head] != s[tail]:
                return False
            
            head += 1
            tail -= 1

        return True