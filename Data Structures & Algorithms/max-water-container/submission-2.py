class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        area = (r-l)* min(heights[l], heights[r])
        while l < r:
            if heights[r] >= heights[l]:
                l += 1
            else:
                r -= 1
            area = max(area, (r-l)* min(heights[l], heights[r]))
        return area
            