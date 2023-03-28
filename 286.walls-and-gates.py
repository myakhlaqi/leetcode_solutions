from collections import deque


def wallsAndGates(rooms):
    """
    The wallsAndGates function will take an array of rooms, and update the array so that all non-wall positions have their distance from a gate.

    :param rooms: Represent the 2d grid
    :return: Nothing
    :doc-author: Trelent
    """
    m = len(rooms)
    n = len(rooms[0])
    gates = [(x // n, x % n)
             for x in range(m * n) if rooms[x // n][x % n] == 0]
    print(gates)

    for i, j in gates:
        q = deque()
        q.append((i, j))

        visited_step = {(i, j : 0}
        while q:
            (x, y) = q.popleft()
            if unvisited_rooms := [(row, col) for row, col in [(x+1, y), (x-1, y), (x, y + 1), (x, y - 1)]
                                   if 0 <= row < m and 0 <= col < n and rooms[row][col] not in {-1, 0} and (row, col) not in visited_step]:
                q.extend(unvisited_rooms)
                parent_step = visited_step[(x, y)]
                visited_step |= ((x, parent_step + 1) for x in unvisited_rooms)
                for i, j in unvisited_rooms:
                    rooms[i][j] = min(rooms[i][j], parent_step+1)

            # print(x, y, q)


# rooms = [[2 ** 31 -1] * 3 for _ in range(4)]
inf = 2 ** 31 - 1
rooms = [[inf, -1, 0, inf],
         [inf, inf, inf, -1],
         [inf, -1, inf, -1],
         [0, -1, inf, inf],

         ]
wallsAndGates(rooms)
for row in rooms:
    print(row)
