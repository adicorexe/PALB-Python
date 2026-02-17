class Solution:
    def findUnion(self, a, b):
        s = set()
        
        for num in a:
            s.add(num)
        for num in b:
            s.add(num)
        
        return list(s)
