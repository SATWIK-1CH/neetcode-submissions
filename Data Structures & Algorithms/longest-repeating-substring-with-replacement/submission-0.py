class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # string s is given and I have to replace any two strings such that the its longer: 
        # so first find the string with longest substring then look around the other sides and replace them
        count={}
        left=0
        max_freq=0
        for right in range(len(s)):
            count[s[right]]=1+count.get(s[right],0)
            max_freq=max(max_freq,count[s[right]])
            if (right-left+1)-max_freq>k:
                count[s[left]]-=1
                left+=1
        return (right-left+1)