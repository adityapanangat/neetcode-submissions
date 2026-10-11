class Solution:
    def maxArea(self, heights: List[int]) -> int:

        left = 0
        right = len(heights) - 1
        area = 0

        while right != left:

            area = max(area, min(heights[left], heights[right]) * (right - left))

            if heights[right] > heights[left]:
                left += 1
            else:
                right -= 1
                

        return area
        

        
        