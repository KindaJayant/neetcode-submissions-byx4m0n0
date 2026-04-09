class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        list.sort(nums)
        return nums[len(nums)//2]
        return    

        
        