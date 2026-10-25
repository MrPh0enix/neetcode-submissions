class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        islands = 0

        def bfs(r, c):
            q = deque()
            visited.add((r, c))
            q.append((r, c))

            dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

            while q:
                r, c = q.popleft()
                for dr, dc in dirs:
                    rN, cN = r+dr, c+dc
                    if (rN in range(ROWS) and
                        cN in range(COLS) and 
                        (rN, cN) not in visited and
                        grid[rN][cN] == '1'):
                        q.append((rN, cN))
                        visited.add((rN, cN))



        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) not in visited and grid[r][c] == '1':
                    bfs(r, c)
                    islands += 1

        return islands