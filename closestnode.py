'''
ou are given a directed graph of n nodes numbered from 0 to n - 1, where each node has at most one outgoing edge.

The graph is represented with a given 0-indexed array edges of size n, indicating that there is a directed edge from node i to node edges[i]. If there is no outgoing edge from i, then edges[i] == -1.

You are also given two integers node1 and node2.

Return the index of the node that can be reached from both node1 and node2, such that the maximum between the distance from node1 to that node, and from node2 to that node is minimized. If there are multiple answers, return the node with the smallest index, and if no possible answer exists, return -1.


'''


class Solution:
    def bfs(self,u, edges):
        n = len(edges)
        min_dist = [-1] * n
        q = dequeue()
        min_dist[u] = 0
        q.append(u)
        while q:
            u = q.popleft()

            if edges[u] != -1:
                next_node = edges[u]
            else:
                return min_dist
            if min_dist[next_node] == -1:
                min_dist[next_node] = min_dist[u]+1
                q.append(next_node)
        return min_dist
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        d1 = self.bfs( node1, edges)
        d2 = self.bfs(node2, edges)
        min_index = -1
        min_dist= float('inf')
        for i in range(len(edges)):
            if min_dist > max(d1[i], d2[i]) and d1[i] != -1 and d2[i]!= -1:
                min_index = i
                min_dist = max(d1[i], d2[i])
    
        return min_index


        
        