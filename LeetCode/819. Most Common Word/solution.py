class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        P = re.sub(r'[^a-zA-Z\s]', ' ', paragraph)
        P = re.sub(r'\s+', ' ', P).strip()

        word_dict = {}
        banned_dict = {word.lower(): True for word in banned}

        for word in P.split(' '):
            word = word.lower()

            if banned_dict.get(word, False):
                continue
            
            word_dict[word] = word_dict.get(word, 0) + 1
        

        word_cnt = [[word, cnt] for word, cnt in word_dict.items()]
        word_cnt.sort(key=lambda x: -x[1])
        most_common_word = word_cnt[0][0]
        return most_common_word