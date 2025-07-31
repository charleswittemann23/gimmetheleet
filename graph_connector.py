from typing import List     
"""
We have two trees (with no cycles, exactly one path between any two nodes) :
Tree A has n nodes labeled 0…n - 1
Tree B has m nodes labeled 0…m - 1
We’re allowed to add one extra edge connecting one node in A to one node in B.
After adding that edge, for each node i in A, we count all nodes (in both A and B) that are at most k steps away from i (moving along the edges given).
We want, for each i, the best possible count we can get by choosing where we should connect with B.


"""

class Solution:

    def buildList(self,edges): ## constructing list that is representative of graph
            n = len(edges) + 1
            adj = [[] for _ in range(n)]
            for u,v in edges:
                adj[v].append(u)
                adj[u].append(v)
            return adj
    def dfs(self,adj,u,p,k): # undirected dfs that allows us to not traverse back on nodes already seen
            if k < 0:
                return 0
            cnt = 1
            for v in adj[u]:
                if v != p: ##checks to make sure we don't go backwards. I.E go back to the node that was we were just sent from
                    cnt+= self.dfs(adj,v, u,k-1)
            return cnt
        
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]], k: int) -> List[int]:
        adj1= self.buildList(edges1)
        adj2 = self.buildList(edges2)

        maxinB = 0 ## focuses on dfs, assuming we traversed to other graph, have k-1 steps to go
        for i in range(len(adj2)):
            maxinB = max(maxinB, self.dfs(adj2,i,-1,k-1))
        res = []

        for i in range(len(adj1)): ## use k steps within the og graph1, and append the optimal path from graph 2
            res.append(self.dfs(adj1, i,-1, k)+ maxinB)
        return res
        

        