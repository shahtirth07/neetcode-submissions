class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
            
        dictionary = {}
        
        for let in s:
            dictionary[let] = dictionary.get(let, 0)+1
        
        for let in t:
            if let not in dictionary:
                return False
            dictionary[let] -= 1

            if dictionary[let] == 0:
                del dictionary[let]
        
        if dictionary == {}:
            return True
        
        return False
