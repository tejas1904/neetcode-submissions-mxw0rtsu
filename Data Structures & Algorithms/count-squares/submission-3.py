from collections import defaultdict
from typing import List

class CountSquares:

    def __init__(self):
        self.g_point_cnt = defaultdict(int)

    def add(self, point: List[int]) -> None:
        self.g_point_cnt[tuple(point)] += 1

    def count(self, point: List[int]) -> int:
        x, y = point
        count = 0

        keys = list(self.g_point_cnt.keys())
        for px, py in keys:

            # same x or same y → cannot be a diagonal
            if px == x or py == y:
                continue

            # must form a square (equal side lengths)
            if abs(px - x) != abs(py - y):
                continue

            # diagonal point
            p1 = (px, py)

            # other two corners
            p2 = (px, y)
            p3 = (x, py)

            count += (
                self.g_point_cnt[p1]
                * self.g_point_cnt[p2]
                * self.g_point_cnt[p3]
            )

        return count