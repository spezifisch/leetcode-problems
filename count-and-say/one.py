class Solution:
    def countAndSay(self, n: int) -> str:
        say = "1"
        i = 1
        while i < n:
            new_say = ""
            pos = 0
            while pos < len(say):
                cpos = pos + 1
                c = say[pos]
                count = 1
                while cpos < len(say) and say[cpos] == c:
                    count += 1
                    cpos += 1

                new_say += str(count) + c
                pos += count

            say = new_say
            i += 1

        return say


# Runtime: 64 ms, faster than 17.96% of Python3 online submissions for Count and Say.
# Memory Usage: 13.1 MB, less than 5.11% of Python3 online submissions for Count and Say.
