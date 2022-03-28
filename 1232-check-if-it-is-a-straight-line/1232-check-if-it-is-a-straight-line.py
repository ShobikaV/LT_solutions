class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        x1,y1=coordinates[0]
        x2,y2=coordinates[1]
        print(x1,y1,x2,y2)
        for x,y in coordinates:
            if (x-x2)*(y1-y2)!=(y-y2)*(x1-x2):
                return(False)
        return(True)