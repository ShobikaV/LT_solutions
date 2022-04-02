class Solution:
    def freqAlphabets(self, s: str) -> str:
        d1 = {str(i-96): str(chr(i)) for i in range(97, 106)}
        d2 = {str(i-96): str(chr(i)) for i in range(106, 123)}

        ans, i = '', 0
		
		# loop through
        while(i < len(s)):
            if((i+2) < len(s) and s[i+2] == '#'):
                ans += d2[str(s[i:i+2])]
                i += 3
            elif d1[str(s[i])]:
                ans += d1[str(s[i])]
                i += 1
                if i == len(s):
                    break
        return ans