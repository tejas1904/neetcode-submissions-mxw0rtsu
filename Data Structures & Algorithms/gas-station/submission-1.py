from typing import List

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)

        for start in range(n):
            tank = 0
            count = 0
            i = start

            while count < n:
                tank += gas[i] - cost[i]
                if tank < 0:
                    break
                i = (i + 1) % n
                count += 1

            if count == n:
                return start

        return -1