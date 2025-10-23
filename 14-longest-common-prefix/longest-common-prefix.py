class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]

        for i in strs[1:]:
            while not i.startswith(prefix):
                prefix = prefix[:-1]
            if not prefix:
                return ""
                for i in strs[2:]:
                    while not i.startswith(prefix):
                        prefix = prefix[:-1]
        
        return prefix 

"""
first word and second word comparison: if there is not a relation between the first two return "" straight 

if not 
compare the first letter 
go on until one of them runs out of words 
if the first two have a common prefix then compare second and third and if the common is the same return it within strings 

"""