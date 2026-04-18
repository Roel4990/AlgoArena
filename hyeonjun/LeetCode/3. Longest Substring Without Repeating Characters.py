class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        check = [1] * len(s)

        if s == "":
            return 0
        else:
            stack = [s[0]]

        for i in range(1, len(s)):
            print(f"i:{i} s:{s[i]} stack:{stack}")
            if s[i] not in stack:
                check[i] = check[i-1] + 1
                stack.append(s[i])
            else:
                stack = stack[stack.index(s[i])+1 :]
                stack.append(s[i])
                check[i] = len(stack)

        return max(check)