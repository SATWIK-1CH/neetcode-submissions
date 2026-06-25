class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for s in strs:
    # Store length + delimiter + content
            res.append(f"{len(s)}#{s}")
        return "".join(res)
    def decode(self, s: str) -> List[str]:
        i=0
        res=[]
        while i<len(s):
            j = s.find('#', i)
            length = int(s[i:j])
            i=j+1
            original_str = s[j + 1 : j + 1 + length]
            res.append(original_str)
            i+=length
        return res