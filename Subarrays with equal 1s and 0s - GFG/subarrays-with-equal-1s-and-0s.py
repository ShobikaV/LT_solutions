#User function Template for python3

class Solution:
    
    #Function to count subarrays with 1s and 0s.
    def countSubarrWithEqualZeroAndOne(self,arr, n):
        d={}
        subsum=0
        count=0
        for i in range(n):
            if arr[i]==0:
                arr[i]=-1
            subsum+=arr[i]
            
            if subsum==0:
                count+=1
            if subsum in d:
                count+=d[subsum]
            d[subsum]=d.get(subsum,0)+1
        return count
        

#{ 
#  Driver Code Starts
#Initial Template for Python 3



def main():
    T=int(input())
    while(T>0):
        
        n=int(input())
        arr=[int(x) for x in input().strip().split()]
        
        obj = Solution()
        print(obj.countSubarrWithEqualZeroAndOne(arr, n))
        
        T-=1

if __name__=="__main__":
    main()
# } Driver Code Ends