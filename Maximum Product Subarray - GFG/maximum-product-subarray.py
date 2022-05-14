#User function Template for python3
class Solution:

	# Function to find maximum
	# product subarray
	def maxProduct(self,arr, n):
		maxi,mini,ans=[arr[0]]*3
		for i in range(1,len(arr)):
		    l=[arr[i],arr[i]*maxi,arr[i]*mini]
		    maxi=max(l)
		    mini=min(l)
		    ans=max(ans,maxi)
		return ans

#{ 
#  Driver Code Starts
#Initial Template for Python 3



if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.maxProduct(arr, n)
        print(ans)
        tc -= 1

# } Driver Code Ends