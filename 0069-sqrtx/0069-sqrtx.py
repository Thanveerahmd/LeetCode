class Solution:
    def mySqrt(self, x: int) -> int:
        (l, r) = (0, x // 2)
        if x < 2:
            return x

        while l <= r:
            mid = (l + r) // 2
            prod = int(mid * mid)
            if prod == x:
                return mid
            elif prod < x:
                l = mid + 1
            else:
                r = mid - 1

        return l - 1 