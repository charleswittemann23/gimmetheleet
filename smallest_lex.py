

"""
You are given two strings of the same length s1 and s2 and a string baseStr.

We say s1[i] and s2[i] are equivalent characters.

For example, if s1 = "abc" and s2 = "cde", then we have 'a' == 'c', 'b' == 'd', and 'c' == 'e'.
Equivalent characters follow the usual rules of any equivalence relation:

Reflexivity: 'a' == 'a'.
Symmetry: 'a' == 'b' implies 'b' == 'a'.
Transitivity: 'a' == 'b' and 'b' == 'c' implies 'a' == 'c'.
For example, given the equivalency information from s1 = "abc" and s2 = "cde", "acd" and "aab" are equivalent strings of baseStr = "eed", and "aab" is the lexicographically smallest equivalent string of baseStr.

Return the lexicographically smallest equivalent string of baseStr by using the equivalency information from s1 and s2.



"""
class Solution:
    def buildGraphWith2Str(self, s1,s2):
            setLettersS1 = set(s1+s2)
            n = len(setLettersS1)
            adj = defaultdict(list)
            for i in range(len(s1)):
                adj[s1[i]].append(s2[i])
                adj[s2[i]].append(s1[i])
            return adj
    def dfs_lex(self, graph, node,visited): ##given a node, return the smallest lexicon character in connected component
        visited.add(node)
        minChar = node

        for newnode in graph[node]:
            if newnode not in visited:
                candidate = self.dfs_lex(graph,newnode, visited)
                minChar = min(minChar, candidate)
        for eachvisit in visited:
            graph[eachvisit] = minChar ## is more optimal , form of memoization, don't need to recompute, can essentially have everyone in graph point to small lex
        return minChar


        

    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        graph = self.buildGraphWith2Str(s1,s2)
        res =''
        for char in baseStr:
            visited =set()
            res += self.dfs_lex(graph, char,visited)
        return res
        

        