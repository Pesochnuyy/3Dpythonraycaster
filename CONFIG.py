#graphics parameters
HEIGHT = 600 
WIDTH = HEIGHT * 2
FPS = 24
BACKGROUND_COLOR = (0, 0, 128)
WALLS_COLOR = (165,42,42)
RAY_COLOR = (255, 0, 0)
#raytracing parameters
NUMBEROFRAYS = 11 #works very weird, i don't know why, maybe you know?
FOV = 70 #degrees, not radians
HALF_FOV = FOV // 2
DEEGRESSES_BETWEENRAYS = FOV / NUMBEROFRAYS
RAY_MAX_LENGHT = 1000 #when program reaches this length, it stops raytracing
RECT_WIDTH = WIDTH / 10
#world parameters
TILE = 20 #size of tile's side
PESOCHNUYYLOGO_COORDS = [37, 42, 39, 44]