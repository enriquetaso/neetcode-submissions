class Solution:
    def amount_water(self, i, j, value1, value2):
        return (j-i) * min(value1, value2)

    def maxArea(self, heights: List[int]) -> int:
        l = 0 
        r = len(heights) - 1
        max_area = 0
        while l < r:
            result = self.amount_water(l, r, heights[l], heights[r])
            if result > max_area:
                max_area = result
            elif heights[l] < heights[r]:
                l +=1
            else:
                r -=1
        return max_area



        