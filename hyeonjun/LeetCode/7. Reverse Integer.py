class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return 0
        num_list = list(str(x))
        if num_list[-1] == 0:
            flag = 0
        else:
            flag = 1
        answer = ""
        
        while num_list:
            s = num_list.pop()
            if s == "0" and flag == 0:
                while num_list[-1] == "0":
                    num_list.pop()
                flag = 1
            elif s != "-":
                answer += s
            else:
                answer = "-" + answer

        answer_i = int(answer)

        return answer_i if answer_i >= -(2**31) and answer_i <= 2**31-1 else 0