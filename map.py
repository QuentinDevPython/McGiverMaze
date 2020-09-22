class Map:

	WIDTH = 15
	LENGHT = 15
	index = 0

	maze_grid = []
	for line_maze_grid in range(LENGHT):
		maze_grid.append([0] * WIDTH)


	#objet_aiguille = tk.PhotoImage(file='ressource/aiguille.png')

	#wall = tk.PhotoImage(file='ressource/wall.png')
	def build_maze_grid(self):
		maze_file = open("maze_grid.txt", "r")
		contenu_maze_file = maze_file.read()
		contenu_maze_file = contenu_maze_file.split()

		for column_maze_grid in range(WIDTH):
			for line_maze_grid in range(LENGHT):
				if (column_maze_grid, line_maze_grid) != (0,0):
					index += 1
				maze_grid[column_maze_grid][line_maze_grid] = contenu_maze_file[index]

		maze_file.close()
    
	