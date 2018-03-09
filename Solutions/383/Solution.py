class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        
        magLetters = {}
        
        # First, construct a hashmap of the letters in magazine.
        for letter in magazine:
            if letter in magLetters:
                magLetters[letter] += 1
            else:
                magLetters[letter] = 1
        
        for letter in ransomNote:
            if letter in magLetters:
                if magLetters[letter] is 0:
                    return False
                else:
                    magLetters[letter] -= 1
            else:
                return False
                
        return True
