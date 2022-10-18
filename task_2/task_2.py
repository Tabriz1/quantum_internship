class Solution:
    def Islands(self, grid):
        if not grid: return 0

        def dfs(i, j, grid):
            if i < 0 or j < 0 or i >= row or j >= col or grid[i][j] == 0:
                return
            grid[i][j] = 0
            dfs(i + 1, j, grid)
            dfs(i - 1, j, grid)
            dfs(i, j + 1, grid)
            dfs(i, j - 1, grid)
            return

        islands = 0
        row = len(grid)
        col = len(grid[0])
        for i in range(0, row):
            for j in range(0, col):
                if grid[i][j] == 1:
                    dfs(i, j, grid)
                    islands += 1
        return islands


n = int(input('row '))
m = int(input('col '))
matrix = []
print("row by row")

for i in range(n):
    a = []
    for j in range(m):
        a.append(int(input()))
    matrix.append(a)

for i in range(n):
    for j in range(m):
        print(matrix[i][j], end=" ")
    print()

print(f'Answer: {Solution().Islands(matrix)}')
