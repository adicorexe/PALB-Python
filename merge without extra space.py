class Solution:
    def mergeArrays(self, arr1, arr2):
        n = len(arr1)
        m = len(arr2)

        gap = (n + m + 1) // 2

        while gap > 0:
            i = 0
            j = gap

            while j < n + m:

                # Case 1: both pointers in arr1
                if i < n and j < n:
                    if arr1[i] > arr1[j]:
                        arr1[i], arr1[j] = arr1[j], arr1[i]

                # Case 2: i in arr1, j in arr2
                elif i < n and j >= n:
                    if arr1[i] > arr2[j - n]:
                        arr1[i], arr2[j - n] = arr2[j - n], arr1[i]

                # Case 3: both in arr2
                else:
                    if arr2[i - n] > arr2[j - n]:
                        arr2[i - n], arr2[j - n] = arr2[j - n], arr2[i - n]

                i += 1
                j += 1

            if gap == 1:
                gap = 0
            else:
                gap = (gap + 1) // 2
