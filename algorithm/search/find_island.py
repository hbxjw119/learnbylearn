#encoding=utf-8

def make_island_area():
    area_map = [
         [0,0,1,0,0,0,0,1,0,0,0,0,0],
         [0,0,0,0,0,0,0,1,1,1,0,0,0],
         [0,1,1,0,1,0,0,0,0,0,0,0,0],
         [0,1,0,0,1,1,0,0,1,0,1,0,0],
         [0,1,0,0,1,1,0,0,1,1,1,0,0],
         [0,0,0,0,0,0,0,0,0,0,1,0,0],
         [0,0,0,0,0,0,0,1,1,1,0,0,0],
         [0,0,0,0,0,0,0,1,1,0,0,0,0]
    ]
    return area_map

def area_dfs(grid, x, y):
    global step
    if x < 0 or y < 0 or x > len(grid) - 1 or y > len(grid[0]) - 1 or grid[x][y] != 1:
        return
    grid[x][y] = -1
    step += 1
    # for i in [[0,1], [1,0], [0, -1], [-1, 0]]:
    area_dfs(grid, x, y + 1)
    area_dfs(grid, x, y - 1)
    area_dfs(grid, x + 1, y)
    area_dfs(grid, x - 1, y)


step = 0
def max_area_island(grid):
    global step
    res = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                step = 0
                area_dfs(grid, i, j)
                res = max(res, step)
    return res


num_island = 0
def max_num_island(grid):
    global num_island
    '''
    visited = []
    for _ in range(len(grid)):
        a = []
        for _ in range(len(grid[0])):
            a.append(False)
        visited.append(a)
    '''
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                num_dfs(grid,  i, j)
                num_island += 1
    return num_island

def num_dfs(grid, x, y):
    if x < 0 or y < 0 or x > len(grid) - 1 or y > len(grid[0]) - 1 or grid[x][y] == -1 or grid[x][y] != 1:
        return
    grid[x][y] = -1
    num_dfs(grid, x, y + 1)
    num_dfs(grid, x, y - 1)
    num_dfs(grid, x + 1, y)
    num_dfs(grid, x - 1, y)


if __name__ == '__main__':
    area = make_island_area()
    print max_area_island(area)
    print max_num_island(area)