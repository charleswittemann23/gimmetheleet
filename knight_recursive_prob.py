"""
Docstring for LeetCode.gimmetheleet.knight_recursive_prob

Problem setup is this, given a knight in the game of chess on n x n board, starting on the square [row, col]. 

Board is 0 indexed where top left square is 0,0 and bottom right cell is (n-1, n-1)

Knight does exactly k moves, with equal chance of performing one of its 8 possible moves, what is the probability
that it finishes on a square in the board.
Continues moving until it is off the board. ONCE OFF the board, no ability to return back on.

"""
class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        moves = [(2,1), (1,2), (-2,1), (-1,2), (2,-1), (1,-2),(-2,-1), (-1,-2)]
        ## eight moves in total possible for every kth iteration. Total possible moves is 8 **k

        ## is n x n board, bounds should be (0,0) and (n-1, n-1)

        dp = [[0] * n for _ in range(n)]
        dp[row][column] = 1 ## guranteed we will start at this position always
        print(dp)

        for step in range(k):
            new_dp = [[0] * n for _ in range(n)]
            for x in range(n):
                for c in range(n):
                    if dp[x][c] > 0:
                        for nh, nv in moves:
                            if 0<= x + nh < n and 0<= c+nv <n: ## first iteration, for any piece that takes move that leaves them on the board has 1/8 chance of happening, use dp to keep track of likelihood of this first iteration, then next iteration, move from those 8 spots, keep making new dp with updated probs, until finally sum up all probabilities
                                new_dp[x+nh][c+nv] += dp[x][c]/8

            dp = new_dp
            
        print(dp)
        return sum(map(sum, dp)) ## need to map because list of lists

if __name__ == '__main__':
     s = Solution()
     print(f"Solution answer: {s.knightProbability(3,2,0,0)}, Expected answer:  0.06250")