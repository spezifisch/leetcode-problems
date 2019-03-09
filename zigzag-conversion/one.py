class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        
        stacks = []
        go_down = True
        i = 0
        while i < len(s):
            if go_down:
                go_down = False
                substr = s[i:i+numRows]
                if len(substr) < numRows:
                    spaces = numRows - len(substr)
                    substr += " " * spaces
                i += numRows
            else:
                go_down = True
                substr = " " + s[i:i+numRows-2] + " "
                substr = substr[::-1]
                if len(substr) < numRows:
                    spaces = numRows - len(substr)
                    substr = " " * spaces + substr
                i += numRows - 2
            
            stacks.append(substr)
            
        #print(stacks)
        
        ret = ""
        for i in range(numRows):
            ret += "".join([stack[i] for stack in stacks])

        return ret.replace(" ", "")
        
# Runtime: 96 ms, faster than 62.38% of Python3 online submissions for ZigZag Conversion.
# Memory Usage: 13.4 MB, less than 9.88% of Python3 online submissions for ZigZag Conversion.

