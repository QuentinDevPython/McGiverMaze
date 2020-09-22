import tkinter as tk 
import pygame

class Main:

	pygame.init()

	# Attributs

	WIDTH = 15
	LENGHT = 15
	index = 0

	maze_grid = []
	for longueur in range(LENGHT):
		maze_grid.append([0] * WIDTH)



	#objet_aiguille = tk.PhotoImage(file='ressource/aiguille.png')

	#wall = tk.PhotoImage(file='ressource/wall.png')



	# Fonctions

	"""def __init__(self):
		self.tiles["9"] = pygame.image.load("ressource/wall.png")
		self.tiles["1"] = pygame.image.load("ressource/wall.png")
		self.tiles["0"] = pygame.image.load("ressource/wall.png")
		self.tiles["2"] = pygame.image.load("ressource/wall.png")"""



	"""
				for y in range(15):
			            for x in range(15):
			                if self.grid[x][y] != "0":
			                    self.screen.blit(self.tiles[self.grid[x][y]], (x*30, y*30))"""


    # Ouverture et lecture du fichier contenant le labyrinthe pour le stocker dans un tableau 2D
    # Map
    
	maze_file = open("maze_grid.txt", "r")
	contenu_maze_file = maze_file.read()
	contenu_maze_file = contenu_maze_file.split()

	for largeur in range(15):
		for longueur in range(15):
			if (largeur, longueur) != (0,0):
				index += 1
			maze_grid[largeur][longueur] = contenu_maze_file[index]

	maze_file.close()


	#print(maze_grid)




