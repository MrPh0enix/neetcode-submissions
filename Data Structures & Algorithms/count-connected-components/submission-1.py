class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        conns = defaultdict(list)
        for i, j in edges:
            conns[i].append(j)
            conns[j].append(i)

        visited = set()

        def dfs(node, prev):
            if node in visited:
                return

            visited.add(node)
            
            for conn in conns[node]:
                if conn == prev:
                    continue
                else:
                    dfs(conn, node)

            return

        count = 0
        for i in range(n):
            if i not in visited:
                count += 1
                dfs(i, None)


        return count
        
