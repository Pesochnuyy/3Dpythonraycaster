#Simple raycasting 3D Game
#Made by Pesochnuyy 
#https://github.com/Pesochnuyy

import pygame
import math
from CONFIG import *
from map import *

pygame.init()

clock = pygame.time.Clock()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("3D raycaster by Pesochnuyy")

ypos = 60
angle = 60  
numberofcollides = 0
xpos = 0 # player's parameters

def is_in_wall(x, y, x1, y1, x4, y4):
    return x>=x1 and x<=x4 and y>=y1 and y<=y4 # returns True if point is in wall

def object_is_in_any_wall(objectx, objecty):
    global points
    output = False
    for item in points:
        if is_in_wall(objectx, objecty, item[0], item[1], item[2], item[3]):
            output = True
            #print("object is in wall", str(item))
    return output #checks if point lies on any wall

def r_between_points(x1, y1, x2, y2):
    return math.sqrt((int(x2) - x1)**2 + (y2 - y1)**2) # distance between two points

running = True 
while running:
    screen.fill(BACKGROUND_COLOR)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    for wall in coords:
        pygame.draw.rect(screen, WALLS_COLOR, (wall[0], wall[1], TILE, TILE), 1) # drawing the map

    pygame.draw.circle(screen, "Green", (xpos, ypos), 3) # drawing the player

    y_vector = math.cos(angle) * 5 
    x_vector = math.sin(angle) * 5 # counting sin and cos of player's direction

    keyes = pygame.key.get_pressed()
    if keyes[pygame.K_w]:
        ypos -= y_vector * 0.2
        xpos -= x_vector * 0.2
    if keyes[pygame.K_s]:
        ypos += y_vector * 0.2
        xpos += x_vector * 0.2
    if keyes[pygame.K_a]:
        angle -= 0.1
    if keyes[pygame.K_d]:
        angle += 0.1 # player movement
    


    if angle == 0:
        angle = 360
    if angle > 360:
        angle = 0 # checking if angle is correct


    pointer_x = xpos + x_vector 
    pointer_y = ypos + y_vector # calculating where pointer that shows player's direction should be

    rayx = xpos
    rayy = ypos 
    current_angle = angle - HALF_FOV
    current_lenght = 0 # current ray's parameters
    ray_collisions = [] # list of all ray's collisions coordinates

    for ray in range(NUMBEROFRAYS): # casting rays and appending their's collision points to array
        while not object_is_in_any_wall(rayx, rayy) and current_lenght < RAY_MAX_LENGHT:
            ray_sin = math.sin(current_angle)
            ray_cos = math.cos(current_angle)
            rayx += ray_sin
            rayy += ray_cos
            current_lenght += 1
        else:
            if current_lenght < RAY_MAX_LENGHT:
                ray_collisions.append([rayx, rayy])
            else:
                ray_collisions.append(["NULL", "NULL"])         
        current_lenght = 0
        current_angle += DEEGRESSES_BETWEENRAYS
        rayx = xpos
        rayy = ypos
    for point in ray_collisions:
        if point[0] != "NULL" and point[1] != "NULL":
            pygame.draw.line(screen, RAY_COLOR, (rayx, rayy), (point[0], point[1]), 3)
                

    if object_is_in_any_wall(xpos, ypos):
        pygame.draw.circle(screen, "Red", (rayx, rayy), 3)
    
    current_x = 0
    for point in ray_collisions:
        point_distance = 0
        rectangle_height = 0
        space_between_rectange = 0
        wall_color = list(WALLS_COLOR)
        if point[0] != "NULL" and point[1]!= "NULL":
            point_distance = r_between_points(xpos, ypos, point[0], point[1])
            try:
                rectangle_height = (HEIGHT / point_distance) * 10
            except:
                pass
            space_between_rectange = (HEIGHT - rectangle_height) / 2
            pygame.draw.rect(screen, WALLS_COLOR, (current_x, space_between_rectange, RECT_WIDTH, rectangle_height))
            current_x += RECT_WIDTH
        else:
            current_x += RECT_WIDTH

    pygame.display.update()
    clock.tick(FPS)