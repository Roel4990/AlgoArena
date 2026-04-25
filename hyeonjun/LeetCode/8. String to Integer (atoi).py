class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        s_list = list(s)
        num_list = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        answer = ""
        flag = 0

        for i in range(len(s_list)):
            if i == 0 and s[i] == "-":
                answer += "-"
                continue
            elif i == 0 and s[i] == "+":
                continue
            if s[i] in num_list:
                answer += s[i]
            else:
                break
        
        if answer == "" or answer == "-" or answer == "+":
            answer += "0"

        answer = int(answer)

        if answer <= -(2**31):
            answer = -(2**31)
        elif answer >= 2**31 - 1:
            answer = 2**31 - 1

        return answer
