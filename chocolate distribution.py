class Solution:
    def findMinDiff(self, arr, m):
        n = len(arr)
        if m == 0 or n == 0:
            return 0
        if n < m:
            return -1
        
        arr.sort()
        min_diff = float('inf')
        
        for i in range(n - m + 1):
            diff = arr[i + m - 1] - arr[i]
            if diff < min_diff:
                min_diff = diff
        
        return min_diff
