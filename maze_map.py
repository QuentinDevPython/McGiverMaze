class Map:

	WIDTH = 15
	LENGHT = 15
	index = 0

	maze_grid = []
	for line_maze_grid in range(LENGHT):
		maze_grid.append([0] * WIDTH)

	maze_file = open("maze_grid.txt", "r")
	contenu_maze_file = maze_file.read()
	contenu_maze_file = contenu_maze_file.split()

	for column_maze_grid in range(WIDTH):
		for line_maze_grid in range(LENGHT):
			if (column_maze_grid, line_maze_grid) != (0,0):
				index += 1
			maze_grid[column_maze_grid][line_maze_grid] = contenu_maze_file[index]

	maze_file.close()

	def get_position_player():
		for column_maze_grid in range(Map.WIDTH):
			for line_maze_grid in range(Map.LENGHT):
				if Map.maze_grid[column_maze_grid][line_maze_grid] == "1":
					return line_maze_grid,column_maze_grid

	def get_position_Guardian():
		for column_maze_grid in range(Map.WIDTH):
			for line_maze_grid in range(Map.LENGHT):
				if Map.maze_grid[column_maze_grid][line_maze_grid] == "2":
					return line_maze_grid,column_maze_grid