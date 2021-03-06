import random
import numpy as np
from game2048.themes import THEMES

def create_grid(): #Crée une grille vide pour l'initialiser
    grid = []
    for i in range(0,4):
        grid.append([' ',' ',' ', ' '])
    return grid

def init_grid(): #Ajoute les premières tuiles sur une grille vide
    grid = create_grid()
    i2,j2 = random.randint(0,3),random.randint(0,3)
    grid[i2][j2] = 2
    i4,j4 = random.randint(0,3),random.randint(0,3)
    while i2 == i4 and j2 == j4:
        i4,j4 = random.randint(0,3),random.randint(0,3)
    grid[i4][j4] = 4
    return grid

def display_grid(grid,theme_number, player_size):
    theme = THEMES[theme_number]
    theme_size_calc = theme_size(theme)
    size = max(theme_size_calc, player_size)
    string = ""
    for i in range(4):
        string += " "
        for j in range(4):
            string += "="*size + " "
        string += "\n|"
        for j in range(4):
            if grid[i][j] == " ":
                string += " "*size + "|"
            else:
                number_size = elem_to_string_size(theme[grid[i][j]])
                string += " "*int((size -number_size)/2) + theme[grid[i][j]] +" "*int(np.ceil((size -number_size)/2)) + "|"
        string += "\n"
    string += " "
    for i in range(4):
        string += "="*size + " "
    return string

def theme_size(theme):
    max = 0
    for case in range(1,14):
        if max < elem_to_string_size(theme[2**case]):
            max = elem_to_string_size(theme[2**case])
    return max

def elem_to_string_size(n):
    if type(n) == type("str"):
        return len(n)
    return int(np.ceil(np.log10(n)))
