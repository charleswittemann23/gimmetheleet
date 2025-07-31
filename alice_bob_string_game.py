class Solution:
    def kthCharacter(self, k: int, operations: List[int]) -> str:
        n, i = 1,0
        while n < k: ## see how many iterations are needed
            n*=2
            i+=1
        d=0 
        while n > 1: ##from total iterations needed, we work backwards seeing if the character we need is changed by operation, keeping track of where it came from in previous first half
            if k > (n // 2):
                k -= n // 2
                d += operations[i-1]
            n //= 2
            i-= 1
        return chr(d % 26 + ord("a"))