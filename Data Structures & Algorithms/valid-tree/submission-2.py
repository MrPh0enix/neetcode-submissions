class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        conns = defaultdict(list)
        for i,c in edges:
            conns[i].append(c)
            conns[c].append(i)

        visited = set()

        def dfs(node, prev):
            if node in visited:
                return False

            visited.add(node)
            for conn in conns[node]:
                if conn == prev:
                    continue
                if not dfs(conn, node):
                    return False

            return True

        if not dfs(0, None):
            return False
        elif len(visited) != n:
            return False
        else:
            return True

