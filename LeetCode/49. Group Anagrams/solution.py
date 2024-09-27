class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        key_dict = {}

        for word in strs:
            sorted_word = ''.join(sorted(word))

            items = key_dict.get(sorted_word, [])
            items.append(word)
            key_dict[sorted_word] = items
        
        return [value for value in key_dict.values()]