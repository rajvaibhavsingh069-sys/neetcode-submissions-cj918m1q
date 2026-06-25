class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hashof_s = {}
        hashof_t ={}
        for i in range(len(s)):
            hashof_s[s[i]]= 1+hashof_s.get(s[i],0)
            hashof_t[t[i]]= 1+hashof_t.get(t[i],0)
        return hashof_s==hashof_t        