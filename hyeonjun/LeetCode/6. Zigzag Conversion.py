class Solution:
    def convert(self, s: str, numRows: int) -> str:
        answer_list = [["" for _ in range(len(s))] for _ in range(numRows)]
        answer = ""
        cur = [0, 0]
        flag = 0

        if numRows == 1:
            return s

        for i in range(len(s)):
            answer_list[cur[0]][cur[1]] = s[i]

            if cur[0] < numRows-1 and flag == 0:
                cur[0] += 1
            elif cur[0] == numRows - 1:
                flag = 1
                cur[0] -= 1
                cur[1] += 1
            elif cur[0] > 0 and flag == 1:
                cur[0] -= 1
                cur[1] += 1
            elif cur[0] == 0 and flag == 1:
                flag = 0
                cur[0] += 1
            else:
                print(error)
                return
        #print(answer_list)

        for i in answer_list:
            for j in i:
                if j != "": answer += j

        return answer