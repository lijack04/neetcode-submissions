class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        par = [i for i in range(n)]
        rank = [1] * n

        def find(n1):
            res = n1
            while res != par[res]:
                par[res] = par[par[res]]
                res = par[res]
            return res
        
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            if p1 == p2:
                return 0
            
            if rank[p2] > rank[p1]:
                par[p1] = p2
                rank[p2] += rank[p1]
            else:
                par[p2] = p1
                rank[p1] += rank[p2]
            return 1
        
        res = n
        for n1, n2 in edges:
            res -= union(n1, n2)
        
        return res
        
        
        # if not n:
        #     return 1
        # if not edges:
        #     return n
        # ROWS, COLS = len(edges), len(edges[0])
        # visited = set()
        # adjList = {i:[] for i in range(n)}
        # for a, b in edges:
        #     adjList[a].append(b)
        #     adjList[b].append(a)

        # def dfs(node, prevN):
        #     if node in visited:
        #         return
        #     visited.add(node)
        #     for adj in adjList[node]:
        #         if adj == prevN:
        #             continue
        #         dfs(adj, node)
        #     return
        
        # res = 0
        # for i in range(n):
        #     if i not in visited:
        #         res += 1
        #     dfs(i, -1)
        
        # return res 
