class Solution:            
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zero_index = {}
        zero_index_cnt = 0
        arr_multiple = 1

        for idx, num in enumerate(nums):
            if num == 0:
                zero_index[str(idx)] = True
                zero_index_cnt += 1
            else:
                arr_multiple *= num
        

        answer = []

        for idx, num in enumerate(nums):
            if zero_index_cnt == 0:
                answer.append(arr_multiple // num)
            elif zero_index_cnt == 1:
                if zero_index.get(str(idx), False):
                    answer.append(arr_multiple)
                else:
                    answer.append(0)
            else:
                answer.append(0)

        return answer
