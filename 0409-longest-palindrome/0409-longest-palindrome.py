class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = {}
        ans = 0
        odd = False
        for ch in s:
            if ch in count:
                count[ch] += 1
            else:
                count[ch] = 1
            
        for frequency in count.values():
                if frequency % 2 == 0:
                    ans += frequency 
                else:
                    ans += frequency - 1
                    odd = True
        if odd:
            ans += 1

        return ans
        


               
                    


            


        