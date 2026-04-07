from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0] * n
        stack = []  # stores indices

        for i in range(n - 1, -1, -1):
            t = temperatures[i]

            # Remove all colder or equal temps
            while stack and temperatures[stack[-1]] <= t:
                stack.pop()

            # If stack not empty → next warmer day exists
            if stack:
                res[i] = stack[-1] - i

            # Push current index
            stack.append(i)

        return res