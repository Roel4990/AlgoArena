class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left+1:right]
        
        result = ""
        for i in range(len(s)):
            odd = expand(i, i)       # 홀수
            even = expand(i, i+1)    # 짝수
            result = max(result, odd, even, key=len)
            print(f"index:{i}, odd:{odd}, even:{even}, result:{result}")
        return result