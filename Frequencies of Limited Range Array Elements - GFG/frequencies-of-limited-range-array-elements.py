class Solution:
    #Function to count the frequency of all elements from 1 to N in the array.
    def frequencyCount(self, arr, N, P):
        '''
        d={}
        l=[]
        for i in range(1,N+1):
            d[i]=arr.count(i)
        for i in d.values():
            l.append(i)
        return l
'''
        d={}
        for i in range(N):
            if arr[i] not in d:
                d[arr[i]]=1
            else:
                d[arr[i]]+=1
        j=0
        for i in range(1,N+1):
            if i not in d:
                arr[j]=0
            else:
                arr[j]=d[i]
            j+=1
        return arr


#{ 
#  Driver Code Starts
#Initial Template for Python 3

import math
if __name__=="__main__":
	T=int(input())
	while(T>0):
		N=int(input())
		arr=[int(x) for x in input().strip().split()]
		P=int(input())
		ob=Solution()
		ob.frequencyCount(arr, N, P)
		for i in arr:
			print(i, end=" ")
		print()
		T-=1



# } Driver Code Ends