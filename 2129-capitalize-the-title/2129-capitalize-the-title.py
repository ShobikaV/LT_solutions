class Solution:
    def capitalizeTitle(self, title: str) -> str:
        ans=[]
        l=title.split()
        for i in range(len(l)):
            a=len(l[i])
            if(a>2):
                b=l[i].capitalize()
                ans.append(b)
            else:
                c=l[i].lower()
                ans.append(c)
        return(" ".join(ans))