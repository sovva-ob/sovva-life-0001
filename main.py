
grid = [
    [0, 1, 0],
    [1, 1, 1],
    [0, 0, 1]
]

for row in grid:
    for cell in row:
        if cell == 1:
            print("alive")
        else:
            print("dead")

def count_neighbors(grid, row, col):
    auto_neighbors = 0

    for dr in range(-1, 2):
        for dc in range(-1, 2):
            if dr == 0 and dc == 0:
                continue
            
            neighbor_row = row + dr
            neighbor_col = col + dc
            
            if 0 <= neighbor_row < len(grid) and 0 <= neighbor_col < len(grid[neighbor_row]):
                auto_neighbors += grid[neighbor_row][neighbor_col]
    return auto_neighbors

row = 1
col = 1

neighbors = count_neighbors(grid, row, col)
print(neighbors)

cell = grid[0][0]
neighbors = count_neighbors(grid, 0, 0)

#    CONWAY'S RULES    #

if cell == 1 and neighbors < 2:
    print("cell dies")

if cell == 1 and (neighbors == 2 or neighbors == 3):
    print("cell survives")

if cell == 1 and neighbors > 3:
    print("cell dies from overpopulation")

if cell == 0 and neighbors == 3:
    print("cell becomes alive")
    grid[0][0] - 1

print(grid[0])