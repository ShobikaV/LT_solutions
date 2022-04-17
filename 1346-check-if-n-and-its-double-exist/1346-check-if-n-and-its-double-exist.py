class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        arr.sort()
        for i in arr:
            if 0 in arr :
                arr.remove(0)
            if i*2 in  arr:
                return True 
                break