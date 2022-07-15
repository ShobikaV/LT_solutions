#User function Template for python3

class Solution:
    def rearrange(self,arr, n):
       lstpos = []
       lstneg = []
       lst= []
       for i in arr:
           if(i<0):
               lstneg.append(i)
           if(i>=0):
               lstpos.append(i)
           if(len(lstneg)>0 and len(lstpos)>0):
               lst.append(lstpos.pop(0))
               lst.append(lstneg.pop(0))
               
       if(len(lstpos)>0):
           lst.extend(lstpos)
       else:
           lst.extend(lstneg)
           
       for i in range(n):
           arr[i] = lst[i]

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	tc = int(input())
	while tc > 0:
		n = int(input())
		arr = list(map(int, input().strip().split()))
		ob = Solution()
		ob.rearrange(arr, n)
		for x in arr:
			print(x, end=" ")
		print()
		tc -= 1

# } Driver Code Ends