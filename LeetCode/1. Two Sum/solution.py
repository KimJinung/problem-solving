class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict = {num: idx for idx, num in enumerate(nums)}

        for idx, num in enumerate(nums):
            if target_idx := num_dict.get(target - num, False):
                if idx > target_idx:
                    return [target_idx, idx]
                elif target_idx > idx:
                    return [idx, target_idx]
                else:
                    continue