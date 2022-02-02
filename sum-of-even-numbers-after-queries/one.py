class Solution:
    def sumEvenAfterQueries(self, A: List[int], queries: List[List[int]]) -> List[int]:
        answer = []
        for val, index in queries:
            A[index] += val
            answer.append(sum([x if x & 1 == 0 else 0 for x in A]))

        return answer


# Time Limit Exceeded
