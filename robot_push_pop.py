from collections import Counter

class Solution:
    def robotWithString(self, s: str) -> str:
        """
         t = []

        res =[]

        freq = Counter(s) ##returns a hash map of frequencies. Ex: freq['a'] will return the number of "a"'s found in s
                            ##alternative explanation : items/chars are stored as keys, their freq as values
        def min_char(freq): ## determines minimum char left. Starting with smallest lex, iterates through alphabet until it finds a character
            for i in range(26):
                ch = chr(ord('a')+i)
                if freq[ch] > 0:
                    return ch
            return 'a'
        for ch in s:
            t.append(ch)
            freq[ch]-= 1
            while t and t[-1] <= min_char(freq):
                res.append(t.pop())
        while t:
            res.append(t.pop())

        return ''.join(res)
        
        
        """
        n = len(s)

        ##dp solution

        
    def robotWithString(self, s: str) -> str:
        n = len(s)
        min_suffix = [''for _ in range(n)]
        min_suffix[-1] = s[-1]
        for i in range(n-2,-1,-1):
            min_suffix[i] = min(s[i], min_suffix[i+1])
        
        t = []
        res = []

        for i in range(n):
            t.append(s[i])

            while t and (i == n - 1 or t[-1] <= min_suffix[i + 1]):
                res.append(t.pop()) 
        
        while t:
            res.append(t.pop())
        
        return ''.join(res)



           