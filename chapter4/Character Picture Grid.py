grid=[['.', '.', '.', '.', '.', '.'],['.', 'O', 'O', '.', '.', '.'],['O', 'O', 'O', 'O', '.', '.'],['O', 'O', 'O', 'O', 'O', '.'],['.', 'O', 'O', 'O', 'O', 'O'],['O', 'O', 'O', 'O', 'O', '.'],['O', 'O', 'O', 'O', '.', '.'],['.', 'O', 'O', '.', '.', '.'],['.', '.', '.', '.', '.', '.']]
n=len(grid)
i=len(grid[0])
j=0
t=0
while j<i:
    while t<n:
        print(grid[t][j],end=" ")
        
        t=t+1
    print()
    j=j+1
    t=0