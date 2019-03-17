class Solution:
    def clumsy(self, N: int) -> int:
        opcodes = ["*", "//", "+", "-"]
        answer = [str(N)]
        for i in range(1, N):
            opcode = (i - 1) % 4
            operand = N - i
            answer += [opcodes[opcode], str(operand)]
                
        answer = eval("".join(answer))
                
        lim = -2**31
        if answer < lim:
            return lim
        lim = 2**31 - 1
        if answer > lim:
            return lim
        
        return answer
    
