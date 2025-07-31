from typing import List
class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        min_rolls = [-1] * (n * n +1)
        q = deque()
        min_rolls[1]=0 ## takes 0 rolls to get to first square, because where we start
        q.append(1)
        
        
        while q: ## while the queue isn't empty, or we have places to go
            x = q.popleft() ## take the first item in the queue
            for i in range(1,7): ## iterate through all 6 moves. 
                t = x + i
                if t > n * n: 
                ## if we go off the board, not a possible move, break out of for loop
                    break
                row = (t-1) // n 
                col = (t-1) % n
                ## ex: t=7 means 0th column in row 1
                v = board[n - 1 - row][(n - 1 - col) if (row % 2 == 1) else col]
                y = v if v > 0 else t
                if y == n * n: #need to check if y, which accounts for possible ladder, is equal to last square
                    return min_rolls[x] + 1
                if min_rolls[y] == -1: ## if we haven't seen yet, we have found a min amount of rolls to get to it, so should update matrix
                    min_rolls[y] = min_rolls[x] + 1
                    q.append(y) ## add new location to queue
        return -1