from collections import deque


def BFS(matrix):
    q = deque()
    n = len(matrix[0])
    m = len(matrix)
    # print( list((i // n, i % n) for i  in range(len(matrix) * n ) if matrix[i // n][ i % n ] == 1))

    is_find = False
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] != "#":
                q.append((i, j))
                is_find = True
                break
        if is_find:
            break

    visited = {q[0]: 0}
    step = 0
    while q:
        i, j = q.popleft()
        if unvisited_neighbors := [(row, col) for row, col in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)] if 0 <= row < m and 0 <= col < n and (row, col) not in visited and matrix[row][col] != "#"]:
            q.extend(unvisited_neighbors)
            step += 1
            visited |= ((x, step) for x in unvisited_neighbors)

        # print(matrix[i][j], step, list(map(lambda x: matrix[x[0]][x[1]], q)), "{", ",".join(map(lambda k: f"{matrix[k[0]][k[1]]}:{str(visited[k])}", visited)), "}")

        


# matrix=[[0,1,0,1],[1,1,1,0],[0,1,1,1],[0,0,1,0]]
matrix = [['A', 'B', '#', '#'], ['#', 'C', '#', '#'],
          ['H', 'D', 'E', 'F'], ['#', 'I', '#', 'G']]

BFS(matrix)
