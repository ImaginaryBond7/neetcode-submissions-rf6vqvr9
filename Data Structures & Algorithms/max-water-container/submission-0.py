class Solution:
    def maxArea(self, heights: List[int]) -> int:
        area = 0
        l, r = 0, len(heights) - 1
        for i in range(len(heights)):
            l = i
            r = len(heights) - 1
            while r > l:
                print(l, heights[l], r, heights[r], area)
                if heights[r] >= heights[l]:
                    area = max(area, ((r-l)*heights[l]))
                else:
                    area = max(area, ((r-l)*heights[r]))
                r -= 1
        return area

        
        