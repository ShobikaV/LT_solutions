#User function Template for python3

class Solution:
    def minValue(self, a, b, n):
        a.sort()
        a.reverse()
        b.sort()
        i,prod=0,0
        for i in range(len(a)):
            prod+=a[i]*b[i]
        return prod
        


#{ 
#  Driver Code Starts
#Initial Template for Python 3


def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        b = [int(x) for x in input().strip().split()]
        ob=Solution()
        print(ob.minValue(a, b, n))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends