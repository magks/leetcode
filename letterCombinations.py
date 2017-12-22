from itertools import product
class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not (digits):
            return []
            
        lettersList = []
        outputCombinations = []
        phonePad = { '2': "abc",
                     '3': "def",
                     '4': "ghi",
                     '5': "jkl",
                     '6': "mno",
                     '7': "pqrs",
                     '8': "tuv",
                     '9': "wxyz"
        }
        for d in digits:
            lettersList.append(phonePad[d])
            
        letterTuple = product(*lettersList) #generator yielding cartesian product of *someIterables as tuples
        for letters in letterTuple:
            combination = ''.join( letters )      # itertools.product() yields ('a', 'b'), so need to convert to string
            outputCombinations.append(combination)
        return outputCombinations
