input_file_path01 = "C:\\CODE\\TahmidRaven\\UNI\\CSE221venv\\LAB04\\Task06_input01.txt"
output_file_path01 = "C:\\CODE\\TahmidRaven\\UNI\\CSE221venv\\LAB04\\Task06_output01.txt"

input_file_path02 = "C:\\CODE\\TahmidRaven\\UNI\\CSE221venv\\LAB04\\Task06_input02.txt"
output_file_path02 = "C:\\CODE\\TahmidRaven\\UNI\\CSE221venv\\LAB04\\Task06_output02.txt"

input_file_path03 = "C:\\CODE\\TahmidRaven\\UNI\\CSE221venv\\LAB04\\Task06_input03.txt"
output_file_path03 = "C:\\CODE\\TahmidRaven\\UNI\\CSE221venv\\LAB04\\Task06_output03.txt"

input_file_path04 = "C:\\CODE\\TahmidRaven\\UNI\\CSE221venv\\LAB04\\Task06_input04.txt"
output_file_path04 = "C:\\CODE\\TahmidRaven\\UNI\\CSE221venv\\LAB04\\Task06_output04.txt"

input_file_path05 = "C:\\CODE\\TahmidRaven\\UNI\\CSE221venv\\LAB04\\Task06_input05.txt"
output_file_path05 = "C:\\CODE\\TahmidRaven\\UNI\\CSE221venv\\LAB04\\Task06_output05.txt"


def dfs(grid, r, c, visited):
    if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]) or grid[r][c] == '#' or visited[r][c]:
        return 0

    visited[r][c] = True
    diamonds = 1 if grid[r][c] == 'D' else 0

    diamonds += dfs(grid, r + 1, c, visited)
    diamonds += dfs(grid, r - 1, c, visited)
    diamonds += dfs(grid, r, c + 1, visited)
    diamonds += dfs(grid, r, c - 1, visited)

    return diamonds

def find_max_diamonds(grid):
    rows = len(grid)
    cols = len(grid[0])
    max_diamonds = 0

    visited = [[False for _ in range(cols)] for _ in range(rows)]

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '.' and not visited[r][c]:
                max_diamonds = max(max_diamonds, dfs(grid, r, c, visited))

    return max_diamonds

def GimmeOutputAtOnce(input_file_path, output_file_path):

    with open(input_file_path, 'r') as f:
        R, H = map(int, f.readline().split())
        grid = [f.readline().strip() for _ in range(R)]

    # maximum amount of diamonds
    max_diamonds = find_max_diamonds(grid)

    with open(output_file_path, 'w') as f:
        f.write(str(max_diamonds))


GimmeOutputAtOnce(input_file_path01,output_file_path01)
GimmeOutputAtOnce(input_file_path02,output_file_path02)
GimmeOutputAtOnce(input_file_path03,output_file_path03)
GimmeOutputAtOnce(input_file_path04,output_file_path04)
GimmeOutputAtOnce(input_file_path05,output_file_path05)