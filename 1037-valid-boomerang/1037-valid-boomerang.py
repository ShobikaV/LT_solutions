class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        x1,y1=points[0]
        x2,y2=points[1]
        for x,y in points:
            if (x-x2)*(y1-y2)!=(y-y2)*(x1-x2):
                return(True)
        return(False)