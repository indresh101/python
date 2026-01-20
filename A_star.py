import heapq

def heuristic(a,b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])

def a_star(start,goal,maze):

    open_list = []
    heapq.heappush(open_list,(0,start))
    g = {start:0}
    parent = {}

    while open_list:
        _,current = heapq.heappop(open_list)

        if current == goal:
            path = []
            while current in parent:
                path.append(current)
                current = parent[current]
            path.append(start)
            return path[::-1]
        
        for dx,dy in [(0,1),(0,-1),(1,0),(-1,0)]:
            nx,ny = current[0]+dx , current[1]+dy

            if 0<=nx<4 and 0<=ny<4 and maze[nx][ny] == 0:
                newg = g[current] + 1

                if (nx,ny) not in g or newg < g[(nx,ny)]:
                    g[(nx,ny)] = newg
                    f = newg + heuristic((nx,ny),goal)
                    heapq.heappush(open_list,(f,(nx,ny)))
                    parent[(nx,ny)] = current


if __name__ == "__main__":
    maze = [
        [0, 0, 1, 0],
        [0, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 1, 0, 0]
    ]
    start = (0,0)
    goal = (3,3)

    path = a_star(start,goal,maze)
    print(path)