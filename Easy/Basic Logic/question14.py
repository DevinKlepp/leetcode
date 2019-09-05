class Solution(object):
    def longestCommonPrefix(self, strs):
        if(len(strs) == 0):
            return ""
        if(len(strs) == 1):
            return strs[0]
        
        prefix = strs[0]
        for string in strs: # for words in list
            if(string == ""):
                    return ""
            elif len(prefix) > len(string):
                prefix = string
        
        index = 0
        for i in range(len(prefix)):
            if all([string[i] == prefix[i] for string in strs]):
                index += 1
            else:
                break
        return prefix[:index]
