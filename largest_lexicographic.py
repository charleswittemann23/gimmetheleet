'''
A lot simpler then described. Essentially boiled down to largest substring starting with the largest lexicographic(z - a is order)
Caveat of num friends. With two friends, need to leave space for numFriends-1 other strings of length 1
'''

class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        if numFriends == 1:
            return word

        res = ""
        length = len(word) - numFriends + 1
        for i in range(0, len(word)):
            temp = word[i : i + length]
            if temp > res:
                res = temp
        return res


        
        

        