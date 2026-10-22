class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        if not n:
            return 1
        if not edges:
            return n
        ROWS, COLS = len(edges), len(edges[0])
        visited = set()
        adjList = {i:[] for i in range(n)}
        for a, b in edges:
            adjList[a].append(b)
            adjList[b].append(a)

        def dfs(node, prevN):
            if node in visited:
                return
            visited.add(node)
            # print(visited)
            for adj in adjList[node]:
                # print("here", adj)
                if adj == prevN:
                    continue
                dfs(adj, node)
            return
        
        res = 0
        for i in range(n):
            if i not in visited:
                # print(i)
                res += 1
            dfs(i, -1)
        
        return res 
