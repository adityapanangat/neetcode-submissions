class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        sortedNums = sorted(nums)
        counts = {}
        triplets = set()

        for i in nums:
            if i not in counts:
                counts[i] = 0
            counts[i] += 1

        for i in range(len(nums)):
            left = 0
            right = len(sortedNums) - 1
            answer = []
            needed = -1 * nums[i]

            while left < right:
                sumLeftRight = sortedNums[left] + sortedNums[right]
                

                if sumLeftRight < needed:
                    left += 1
                elif sumLeftRight > needed:
                    right -= 1
                else:
                    answer = [sortedNums[left], sortedNums[right]]
                    numberOfIInAnswer = 0
                    
                    for ger in answer:
                        if ger == nums[i]:
                            numberOfIInAnswer += 1
                    
                    if (numberOfIInAnswer < counts[nums[i]]):
                        triplets.add(tuple(sorted([nums[i],answer[0],answer[1]])))

                    right -= 1
                    left += 1
        
        return list(triplets)