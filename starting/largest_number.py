class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        string=[str(i) for i in nums]
        for x in range(len(string)-1):
            for y in range (x, len(string)):
                if string[x]+string[y]<string[y]+string[x]:
                    string[x],string[y]=string[y],string[x]
        return '0' if string[0] == '0' else ''.join(string)
