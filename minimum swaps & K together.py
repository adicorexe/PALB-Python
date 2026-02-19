class Solution:
    def minSwap(self, arr, k):
        n = len(arr)
        
        good = 0
        for i in range(n):
            if arr[i] <= k:
                good += 1
        
        bad = 0
        for i in range(good):
            if arr[i] > k:
                bad += 1
        
        ans = bad
        
        i = 0
        j = good
        
        while j < n:
            if arr[i] > k:
                bad -= 1
            if arr[j] > k:
                bad += 1
            
            ans = min(ans, bad)
            
            i += 1
            j += 1
        
        return ans
