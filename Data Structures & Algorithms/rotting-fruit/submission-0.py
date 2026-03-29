class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        rotting_fruit = []
        good_fruit_count=  0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    good_fruit_count+=1
                elif grid[i][j]==2:
                    rotting_fruit.append([i,j])
        
        queue = deque(rotting_fruit)
        visited = set()
        for i,j in rotting_fruit:
            visited.add((i,j))

        timestep= 0 
        while queue and good_fruit_count>0:
            for _ in range(len(queue)):
                a,b = queue.popleft()
                for i,j in ((a+1,b),(a-1,b),(a,b+1),(a,b-1)):
                    if 0<=i<len(grid) and 0<=j<len(grid[0]) and grid[i][j]==1 and (i,j) not in visited:
                        queue.append((i,j))
                        visited.add((i,j))
                        good_fruit_count-=1
            timestep+=1
        
        if good_fruit_count<=0:
            return timestep
        else:
            return -1


        