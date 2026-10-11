class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * len(nums)
        
        currentProduct = 1

        #multiply by the prefix
        for i in range(len(nums)):
            output[i] *= currentProduct
            currentProduct *= nums[i]

        currentProduct = 1

        #multiply by the suffix
        for i in range(len(nums) - 1, -1, -1):
            output[i] *= currentProduct
            currentProduct *= nums[i]

        return output