class Solution:
    def maxArea(self, height):
        l = 0  
        r = len(height)-1
        maxArea = 0
        
        while l != r:
            hl = height[l]
            hr = height[r]
            
            width = r-l
            height_capacity = min( hl, hr )
            area = width*height_capacity
            
            maxArea = max(maxArea, area ) 
            
            if hl < hr:
                l += 1
            else:
                r -= 1
            
        return maxArea
        
