class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        n = len(prefix)

        for word in strs[1:]:
            while not word.startswith(prefix):
                prefix = prefix[:-1]
                if word.startswith(prefix):
                    for word in strs[2:]:
                        while not word.startswith(prefix):
                            prefix = prefix[:-1]
            if not prefix:
                return ""
        return prefix

"""
first word and second word comparison: if there is not a relation between the first two return "" straight 

if not 
compare the first letter 
go on until one of them runs out of words 
if the first two have a common prefix then compare second and third and if the common is the same return it within strings 

"""