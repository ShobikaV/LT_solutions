#User function Template for python3

#Function to find a continuous sub-array which adds up to a given number.
class Solution:
    def subArraySum(self,arr, n, s): 
        ss=0
        l,i=0,0
        ans=[]
        while i<n:
            if ss+arr[i]<=s:
                ss+=arr[i]
                i+=1
            else:
                ss-=arr[l]
                l+=1
            if ss==s:
                return [l+1,i]
        return [-1]
        
                
            
        
#{ 
#  Driver Code Starts
#Initial Template for Python 3

import math

def main():
        T=int(input())
        while(T>0):
            
            NS=input().strip().split()
            N=int(NS[0])
            S=int(NS[1])
            
            A=list(map(int,input().split()))
            ob=Solution()
            ans=ob.subArraySum(A, N, S)
            
            for i in ans:
                print(i, end=" ")
                
            print()
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends