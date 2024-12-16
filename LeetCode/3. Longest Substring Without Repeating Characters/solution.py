class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        answer = 0
        cache_value = 0
        cache_mem = {}
        start = 0
        end = len(s)

        while start < end:
            for idx in range(start, end):
                ch = s[idx]

                if next_start := cache_mem.get(ch):
                    cache_mem = {}
                    if cache_value > answer:
                        answer = cache_value
                    cache_value = 0
                    start = next_start
                    break

                cache_mem[ch] = idx + 1
                cache_value += 1

        return answer if answer > cache_value else cache_value