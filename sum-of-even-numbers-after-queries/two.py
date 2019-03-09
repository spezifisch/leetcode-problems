class Solution:
    def sumEvenAfterQueries(self, A: List[int], queries: List[List[int]]) -> List[int]:
        answer = []
        even_sum = sum([x if x % 2 == 0 else 0 for x in A])
        
        for val, index in queries:
            previous_val = A[index]
            A[index] += val
            
            if previous_val % 2 == 0:
                even_sum -= previous_val

            if A[index] % 2 == 0:
                even_sum += A[index]
                
            answer.append(even_sum)
            
        return answer

# Runtime: 200 ms, faster than 13.15% of Python3 online submissions for Sum of Even Numbers After Queries.
# Memory Usage: 17.6 MB, less than 5.56% of Python3 online submissions for Sum of Even Numbers After Queries.

