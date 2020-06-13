class Solution(object):

    def maxArea_brutforce(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        area = {}
        maxx = -1
        for i in range(len(height)):
        	for j in range(i, len(height)):

        		area[i, j] = min(height[i], height[j]) * (j-i)
        		maxx = max(area[i, j], maxx)

        (i, j) = [k for k, v in area.items() if v == maxx]

        return maxx

    def maxArea_pointers (self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        area = {}
        maxx = -1

        while i < j:

        	area[i, j] = min(height[i], height[j]) * (j-i)
        	maxx = max(area[i, j], maxx)

        	if height[i] < height[j]:
        		i += 1
        	else:
        		j -= 1


        return maxx
