class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()
        i,j,count=0,0,0
        for i in range(len(seats)):
            count+=abs(seats[i]-students[j])
            j+=1
        return count