class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        c=0
        m=intervals[0][1]
        for i in range(1,len(intervals)):
            a=intervals[i]
            if m>a[0]:
                m=min(m,a[1])
                #intervals.pop(i+1)
                c+=1
            else:
                m=a[1]
        return c
            