def maxAreaOfIsland(grid) -> int:
    visited = [[0] * len(grid[0]) for x in range(len(grid))]
    answer = 0
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1 and visited[i][j] == 0:
                queue = list()
                visit = set()
                queue.append((i, j))
                visit.add((i, j))
                while queue:
                    node = queue.pop(0)
                    if visited[node[0]][node[1]] == 0:
                        visited[node[0]][node[1]] = 1
                        for k in range(4):
                            if 0 <= node[0] + dx[k] < len(grid) and 0 <= node[1] + dy[k] < len(grid[0]) and grid[node[0] + dx[k]][node[1] + dy[k]] == 1:
                                queue.append((node[0] + dx[k], node[1] + dy[k]))
                                visit.add((node[0] + dx[k], node[1] + dy[k]))
                answer = max(answer, len(visit))
    return answer

if __name__ == '__main__':
    print(6 == maxAreaOfIsland([[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]))