class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adjList = {i:[] for i in range(n)}
        for a, b in edges:
            adjList[a].append(b)
            adjList[b].append(a)
        
        visited = set()

        def dfs(node, lastN):
            if node in visited:
                return False
            
            visited.add(node)
            for adj in adjList[node]:
                if adj == lastN:
                    continue
                if not dfs(adj, node):
                    return False
            return True
        
        return dfs(0, -1) and len(visited) == n