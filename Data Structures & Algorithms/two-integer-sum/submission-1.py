class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n=len(nums)
        hash_map={}

        for i in range(n):
            remainder=target-nums[i]
            if remainder in hash_map:
                return [hash_map[remainder],i]
            hash_map[nums[i]]=i







        