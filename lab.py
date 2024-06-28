import pygame 
import os
from pygame.locals import *


direct = os.path.dirname(__file__)

textures_img_links = direct + '/textures'

pygame.init()
pygame.mixer.init()

SCREEN_WIDTH = 1260
SCREEN_HEIGHT = 560
python_file_path = direct + "/file.py"
#*------------------------------------------------------- картинки
floor_glass = textures_img_links + "/glass.png"
wall = textures_img_links + "/wall.png"
wall_glass = textures_img_links + "/wall_glass.png"
music_path = textures_img_links + '/music'
floor_end = textures_img_links + "/glass_finish.png"

ch_R = textures_img_links + "/sonic.png"
ch_L = textures_img_links + "/sonic_left.png"

tutarial = textures_img_links + '/start_screen_1.png'
normal = textures_img_links + '/start_screen_2.png'
hard = textures_img_links + '/start_screen_3.png'
easy = textures_img_links + '/start_screen_4.png'
madness = textures_img_links + '/start_screen_5.png'
bg = textures_img_links + '/space.png'
bg_start = textures_img_links + '/start_screen.png'
icon = textures_img_links + '/icon2.ico'

music_bg = music_path + '/background_sound.mp3'
music_w = music_path + '/win.mp3'
music_E = music_path + '/end.mp3'
music_menu = music_path + '/start_up_music.mp3'
music_button_menu = music_path + '/menu_accept.mp3'
music_menu_pick_levels = music_path + '/menu.mp3'

icon = pygame.image.load(icon)
bg_start = pygame.image.load(bg_start)
bg = pygame.image.load(bg)
tutarial = pygame.image.load(tutarial)
normal = pygame.image.load(normal)
hard =  pygame.image.load(hard)
easy =  pygame.image.load(easy)
madness = pygame.image.load(madness)
ch_R = pygame.image.load(ch_R)
ch_L = pygame.image.load(ch_L)
floor_end = pygame.image.load(floor_end)
floor_glass = pygame.image.load(floor_glass) 
wall = pygame.image.load(wall)
wall_glass = pygame.image.load(wall_glass)

icon = pygame.transform.scale(icon, (32, 32))
ch_R = pygame.transform.scale(ch_R, (20, 25))
ch_L = pygame.transform.scale(ch_L, (20, 25))
tutarial = pygame.transform.scale(tutarial, (SCREEN_WIDTH, SCREEN_HEIGHT))
normal = pygame.transform.scale(normal, (SCREEN_WIDTH, SCREEN_HEIGHT))
hard =  pygame.transform.scale(hard, (SCREEN_WIDTH, SCREEN_HEIGHT))
easy = pygame.transform.scale(easy, (SCREEN_WIDTH, SCREEN_HEIGHT)) 
madness = pygame.transform.scale(madness, (SCREEN_WIDTH, SCREEN_HEIGHT))
bg_start = pygame.transform.scale(bg_start, (SCREEN_WIDTH, SCREEN_HEIGHT))
bg = pygame.transform.scale(bg, (SCREEN_WIDTH, SCREEN_HEIGHT))

floor_end = pygame.transform.scale(floor_end, (35, 35))
floor_glass = pygame.transform.scale(floor_glass, (35, 35))
wall = pygame.transform.scale(wall, (35, 35))
wall_glass = pygame.transform.scale(wall_glass, (35, 35))
#*------------------------------------------------------- картинки

character = ch_R

clock_game = pygame.time.Clock()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Sonic the Hedgehog: Labyrinth Edition")
pygame.display.set_icon(icon)

player = pygame.Rect(0, 0, 20, 20)

font = pygame.font.Font(textures_img_links + "/soniclogo_jp.ttf", 45)
font_little = pygame.font.Font(textures_img_links + "/soniclogo_jp.ttf", 20)

start = font.render("Play", True, (235, 235, 235))
title = font.render("Select difficulty mode:", True, (235, 235, 235))
end = font.render("The End!", True, (207, 207, 207))

easy_S = font.render("Easy mode", True, (84, 217, 13))
normal_S = font.render("Normal mode", True, (245, 197, 7))
hard_S = font.render("Hard mode", True, (212, 13, 13))
madness_S = font.render("Madness mode", True, (219, 15, 216))
back = font.render("<---", True, (0, 0, 0))
#font = pygame.font.SysFont("Arial", 50)
#text = font.render("The End! Thanks for the game!!!!", True, (32, 107, 227))
finish = 0

info_about_modes = {
    "Easy" : {
        "0": "Easy Mode is the simplest level designed for beginners' training.",
        "1": "The main objective is to reach the finish line.",
        "2": "There are no difficulties on this level, only maximum ease!",
    },

    "Normal": {
        "0":"The normal or classic level is also considered easy,",
        "1": "but less so than the previous one.",
        "2": "Objective: reach the finish line.",
    },
    
    "Hard": {
        "0": "Hard level - you won't pass on your first attempt, requiring numerous tries.",
        "1": "Filled with traps and complexity surpassing the previous level by four difficulty levels.",
        "2": "Objective: reach the finish line."
    },

    "Madness": {
        "0": "Madness mode is a mix of previous levels, creating one challenging level.",
        "1": "This level will make you sweat! Not for beginners; complete the easy mode first!",
        "2": "Goal: Reach the finish line without crashing your computer."
    }
}

#проверка ходьбы на ...
go_R = False
go_L = False
go_UP = False
go_D = False

step = 6
run = 10
movie = step
start_screen = 1 

All_textures = {
    "easy": [ #! 36x16
    [0, 0, 1, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 2, 0, 0, 2, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
    [0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 1],
    [0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 2, 0, 0, 1, 0, 0, 1, 0, 0, 2, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1],
    [0, 0, 1, 0, 0, 1, 0, 0, 2, 0, 0, 2, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1],
    [0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 2, 0, 0, 1, 0, 0, 1, 0, 0, 2, 0, 0, 2, 0, 0, 1, 0, 0, 1, 0, 0, 2, 0, 0, 1],
    [0, 0, 1, 0, 0, 1, 0, 0, 2, 0, 0, 2, 0, 0, 2, 0, 0, 2, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 1],
    [0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 2, 0, 0, 1, 0, 0, 1, 0, 0, 2, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1],
    [0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 2, 0, 0, 2, 0, 0, 1, 0, 0, 2, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 1],
    [0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 2, 0, 0, 1, 0, 0, 1, 0, 0, 2, 0, 0, 2, 0, 0, 1, 0, 0, 1, 0, 0, 2, 0, 0, 1],
    [0, 0, 1, 0, 0, 1, 0, 0, 2, 0, 0, 2, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1],
    [0, 0, 1, 0, 0, 1, 0, 0, 2, 0, 0, 2, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 2, 0, 0, 1],
    [0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 2, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 2, 0, 0, 1, 0, 0, 1, 0, 0, 2, 0, 0, 1],
    [0, 0, 1, 0, 0, 1, 0, 0, 2, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 2, 0, 0, 1, 0, 0, 1, 0, 0, 2, 0, 0, 1],
    [0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 2, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1],
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 3, 3, 1],
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 3, 3, 1]
],
    "normal": [ #! 36x16
    [1, 0, 0, 2, 1, 1, 2, 2, 2, 1, 1, 2, 2, 1, 1, 2, 1, 1, 2, 2, 2, 1, 1, 2, 2, 2, 1, 2, 1, 1, 2, 1, 2, 3, 3, 1],
    [2, 0, 0, 1, 1, 2, 2, 1, 1, 2, 2, 1, 2, 1, 1, 1, 2, 2, 2, 1, 2, 1, 2, 1, 2, 2, 1, 1, 2, 2, 1, 2, 1, 0, 0, 1],
    [2, 0, 0, 0, 0, 0, 1, 2, 1, 1, 1, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 1, 2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 1, 1, 2, 2, 2, 2, 1, 1, 1, 0, 0, 2],
    [2, 2, 1, 2, 0, 0, 2, 2, 2, 1, 1, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 2, 2, 1, 2, 1, 2, 2, 0, 0, 0, 0, 1],
    [1, 1, 2, 2, 0, 0, 2, 1, 1, 2, 2, 2, 1, 0, 0, 0, 0, 0, 0, 2, 0, 0, 2, 2, 2, 1, 1, 2, 2, 1, 1, 0, 0, 0, 0, 2],
    [0, 0, 0, 0, 0, 0, 1, 1, 2, 2, 1, 1, 1, 0, 0, 1, 2, 2, 2, 1, 0, 0, 1, 1, 2, 2, 1 ,2, 2, 1, 2, 0, 0, 1, 2, 2],
    [0, 0, 0, 0, 0, 0, 1, 2, 2, 1, 1, 1, 2, 0, 0, 1, 1, 2, 1, 2, 0, 0, 2, 1, 1, 2, 2, 1, 2, 1, 1, 0 ,0, 1, 2, 2],
    [0, 0, 2, 2, 1, 1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 2, 2, 1, 0, 0, 2, 2, 1, 2, 1, 1, 1, 2, 2, 0, 0, 2, 1, 1],
    [0, 0, 2, 2, 1, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 2, 1, 1, 2, 2, 0, 0, 1, 1, 1, 2, 2, 1, 1, 1, 2, 0, 0, 1, 1, 2],
    [0, 0, 0, 0, 2, 2, 1, 2, 0, 0, 1, 1, 1, 1, 2, 1, 2, 1, 1, 2, 0, 0, 2, 2, 2, 1, 1, 1, 2, 2, 1, 0, 0, 2, 1, 1],
    [0, 0, 0, 0, 1, 1, 2, 1, 0, 0, 1, 1, 2, 2, 1, 2, 1, 2, 2, 1, 0, 0, 1, 1, 1, 1, 2, 2, 1, 2, 2, 0, 0, 1, 1, 2],
    [1, 1, 0, 0, 2, 2, 1, 2, 0, 0, 1, 2, 2, 1, 2, 1, 2, 1, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 1],
    [1, 2, 0, 0, 1, 1, 2, 1, 0, 0, 1, 2, 1, 1, 2, 2, 1, 2, 1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 1],
    [2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 2, 1, 2, 2, 1, 2, 2, 1, 1, 2, 1, 1, 2, 2, 1, 2, 2, 2, 1, 1, 1, 2, 2],
    [2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 2, 1, 1, 1, 2, 2, 1, 2, 2, 1, 1, 2, 2, 1, 2 ,1, 2 ,1, 2, 1, 2, 1, 2, 2]
],
    "hard": [ #! 36x16
    [1, 0, 1, 2, 1, 1, 2, 2, 2, 1, 1, 2, 2, 1, 1, 2, 1, 1, 2, 2, 2, 1, 1, 2, 2, 2, 1, 2, 1, 1, 2, 1, 2, 2, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [2, 2, 1, 2, 2, 1, 2, 2, 1, 1, 1, 1, 1, 2, 1, 2, 0, 0, 0, 2, 2, 1, 1, 1, 2, 2, 1, 2, 2, 1, 2, 1, 1, 2, 1, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [2, 0, 1, 2, 2, 1, 2, 1, 1, 2, 1, 2, 2, 1, 1, 2, 1, 1, 2, 2, 2, 1, 1, 1, 1, 2, 1, 2, 1, 1, 2, 2, 2, 1, 1, 1],
    [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 1],
    [1, 1, 1, 2, 1, 1, 2, 1, 1, 2, 1, 2, 2, 1, 1, 2, 2, 1, 2, 1, 2, 1, 1, 1, 2, 1, 1, 2, 2, 1, 2, 2, 1, 0, 1, 0],
    [1, 1, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2],
    [1, 0, 1, 2, 0, 1, 2, 1, 1, 0, 1, 0, 2, 1, 1, 2, 1, 1, 2, 1, 2, 1, 1, 2, 2, 1, 1, 2, 1, 1, 2, 1, 2, 1, 1, 2],
    [2, 0, 1, 2, 0, 1, 2, 1, 2, 1, 1, 2, 1, 0, 1, 2, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 2, 0, 0, 0, 1, 0],
    [2, 0, 1, 2, 0, 1, 2, 1, 2, 1, 1, 0, 0, 0, 1, 2, 0, 1, 2, 2, 0, 0, 1, 0, 0, 2, 1, 2, 0, 1, 2, 0, 2, 0, 1, 0],
    [2, 0, 1, 2, 0, 1, 2, 2, 1, 0, 0, 0, 1, 0, 1, 2, 0, 1, 2, 2, 0, 0, 1, 0, 0, 2, 1, 2, 0, 1, 2, 0, 2, 0, 1, 0],
    [2, 0, 1, 2, 0, 1, 2, 1, 2, 0, 1, 1, 1, 0, 1, 2, 0, 1, 2, 1, 0, 0, 1, 0, 0, 2, 1, 2, 0, 1, 2, 0, 2, 0, 1, 0],
    [2, 0, 1, 2, 0, 1, 2, 1, 0, 0, 1, 2, 2, 0, 1, 2, 0, 1, 2, 1, 0, 0, 1, 0, 0, 1, 1, 2, 0, 1, 2, 0, 1, 3, 1, 0],
    [1, 0, 1, 2, 0, 1, 1, 0, 0, 2, 1, 1, 0, 0, 0, 0, 0, 1, 2, 1, 0, 0, 0, 0, 0, 1, 1, 2, 0, 0, 0, 0, 1, 3, 1, 0],
    [1, 0, 1, 2, 0, 0, 0, 0, 2, 1, 1, 2, 1, 1, 1, 2, 0, 1, 2, 1, 2, 2, 1, 1, 2, 1, 1, 2, 2, 1, 2, 2, 1, 3, 1, 0]
],
    "madness": [ #! 36x16
    [2, 0, 0, 1, 2, 2, 2, 0, 0, 0, 2, 1, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 2, 2, 2, 2],
    [1, 1, 0, 0, 1, 2, 2, 0, 1, 0, 1, 2, 0, 1, 2, 0, 1, 0, 2, 1, 2, 2, 1, 0, 1, 0, 1, 1, 2, 2, 0, 2, 2, 1, 1, 1],
    [1, 2, 2, 0, 1, 1, 2, 0, 1, 0, 0, 2, 0, 2, 2, 0, 1, 0, 1, 2, 2, 1, 2, 0, 0, 0, 2, 2, 1, 1, 0, 1, 2, 2, 1, 2],
    [1, 2, 1, 0, 0, 1, 2, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 2, 1, 2, 2, 1, 1, 2, 1, 2, 2, 1, 0, 2, 2, 1, 1, 1],
    [2, 2, 2, 1, 0, 0, 2, 2, 0, 1, 1, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 2, 1, 1, 1, 0, 1, 2, 1, 2, 2],
    [1, 1, 2, 1, 2, 0, 0, 1, 0, 0, 0, 0, 0, 1, 2, 2, 1, 1, 2, 1, 1, 2, 2, 1, 1, 2, 2, 2, 2, 2, 0, 1, 1, 2, 1, 1],
    [2, 2, 1, 2, 1, 2, 0, 1, 1, 1, 2, 2, 0, 0, 1, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 0, 1, 2, 2, 1, 1],
    [1, 1, 1, 2, 2, 0, 0, 2, 2, 1, 0, 0, 0, 1, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 1, 0, 1, 2, 2, 1, 1],
    [2, 1, 2, 1, 0, 0, 1, 1, 1, 2, 0, 1, 1, 2, 2, 2, 1, 1, 2, 1, 2, 1, 2, 1, 2, 2, 1, 1, 1, 1, 0, 1, 2, 1, 2, 2],
    [1, 1, 1, 2, 0, 1, 1, 2, 2, 0, 0, 1, 2, 2, 2, 2, 1, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 2, 1, 2, 3, 1, 2, 2, 2, 2],
    [2, 2, 1, 1, 0, 1, 2, 1, 2, 0, 1, 2, 2, 1, 1, 1, 1, 1, 2, 2, 1, 1, 2, 1, 2, 2, 2, 2, 2, 1, 2, 1, 1, 1, 1, 1],
    [1, 2, 1, 0, 0, 1, 2, 1, 1, 0, 0, 0, 0, 0, 0, 0, 2, 2, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 1],
    [2, 2, 1, 0, 2, 2, 1, 1, 2, 2, 1, 1, 2, 2, 2, 0, 1, 1, 2, 2, 1, 1, 2, 2, 2, 2, 1, 2, 1, 2, 1, 2, 1, 1, 1, 2],
    [1, 1, 0, 0, 1, 2, 2, 2, 2, 1, 2, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 1, 2, 2, 1, 2, 1, 2, 2, 2, 1, 2, 1, 2, 1, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 0],
    [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
],
}

go_R = False
go_L = False
go_UP = False
go_D = False

#textur_len = len(rects)

runnnig = True

title_coordinnate = (SCREEN_WIDTH / 4.5, 60) 
easy_coordinnate = (SCREEN_WIDTH / 6, 160)
normal_coordinnate = (SCREEN_WIDTH / 5, 260)
hard_coordinnate = (SCREEN_WIDTH / 4, 360)
madness_coordinnate = (SCREEN_WIDTH / 3, 460)

rects = []
rects_TEXTURES = []
bad_rects = []
good_rects = []


def load_textures(x=0, y=0):
    for texture_draw in texture:
            for i in texture_draw:
                cube = pygame.Rect(x, y, 35, 35)
                rects.append(cube)
                rects_TEXTURES.append(i)
                if i == 1 or i == 2:
                    bad_rects.append(cube)
                if i == 3:
                    good_rects.append(cube)
                x += 35
            y += 35
            x = 0 

text = 0

def music_menu_choouse_level():
    pygame.mixer.music.load(music_menu_pick_levels)
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.03)

def music_menu_bg():
    pygame.mixer.music.load(music_menu)
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.03)

click_sound = pygame.mixer.Sound(music_button_menu)
click_sound.set_volume(0.05)

def Green_Hill():
    pygame.mixer.music.load(music_bg)
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.05)

music_menu_bg()
while runnnig:
    pygame.draw.rect(screen, (250, 0, 0), player)
    
    if start_screen != 2 or screen != False:
        screen.blit(bg_start, (0,0))
        screen.blit(start, (50, 460))

    if start_screen == False:
        if text == 0:
            text = 1
        elif text == 1:
            text = 2
        if text == 1:    
            load_textures()
            

        screen.fill((44, 170, 219))

        for i in range(len(rects_TEXTURES)):  
            if rects_TEXTURES[i] == 0:
                screen.blit(floor_glass, rects[i])
            if rects_TEXTURES[i] == 3:
                screen.blit(floor_end, rects[i])
            if rects_TEXTURES[i] == 1:
                screen.blit(wall, rects[i])
            if rects_TEXTURES[i] == 2:
                screen.blit(wall_glass, rects[i])

        screen.blit(character, player)


    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            runnnig = False

        if i.type == pygame.KEYUP:
            if i.key == pygame.K_ESCAPE:
                runnnig = False

        if i.type == pygame.KEYDOWN:
            if i.key == pygame.K_d or i.key == pygame.K_RIGHT:
                go_R = True
            if i.key == pygame.K_a or i.key == pygame.K_LEFT:
                go_L = True
            if i.key == pygame.K_s or i.key == pygame.K_DOWN:
                go_D = True
            if i.key == pygame.K_w or i.key == pygame.K_UP:
                go_UP = True
            if i.key == pygame.K_LSHIFT:
                movie = run 
            if finish != 2:
                if i.key == pygame.K_LCTRL:
                    player.x = 1170
                    player.y = 535

        if i.type == pygame.KEYUP:
            if i.key == pygame.K_d or i.key == pygame.K_RIGHT:
                go_R = False
            if i.key == pygame.K_a or i.key == pygame.K_LEFT:
                go_L = False
            if i.key == pygame.K_s or i.key == pygame.K_DOWN:
                go_D = False
            if i.key == pygame.K_w or i.key == pygame.K_UP:
                go_UP = False   
            if i.key == pygame.K_LSHIFT:
                movie = step

        if start_screen != False:
            if i.type == pygame.MOUSEBUTTONDOWN:
                start_g = start.get_rect(topleft=(50, 460)) 

                easy_S_G = easy_S.get_rect(topleft=easy_coordinnate) 
                normal_S_G = normal_S.get_rect(topleft=normal_coordinnate)
                hard_S_G = hard_S.get_rect(topleft=hard_coordinnate)  
                madness_S_G = madness_S.get_rect(topleft=madness_coordinnate)    

                #back_G = back.get_rect(topleft=(50, 460))

                if start_screen != 2 or finish != 1:
                    print(1)
                    start_g = start.get_rect(topleft=(55, 460))
                    if start_g.collidepoint(i.pos):
                        start_screen = 2
                        pygame.mixer.music.pause()
                        music_menu_choouse_level() 

               #if finish >= 1 and back_G.collidepoint(i.pos):
               #    start_screen = 2
               #    pygame.mixer.music.pause()
               #    music_menu_choouse_level()
               #    print(True)
                if start_screen >= 2:
                        start_g = start.get_rect(topleft=(900, 460))    
                if easy_S_G.collidepoint(i.pos):
                    click_sound.play()
                    start_screen = 3      
                elif normal_S_G.collidepoint(i.pos):  
                    click_sound.play()
                    start_screen = 4         
                elif hard_S_G.collidepoint(i.pos):  
                    click_sound.play()              
                    start_screen = 5
                elif madness_S_G.collidepoint(i.pos): 
                    click_sound.play()              
                    start_screen = 6    

                if start_screen == 3:
                    if start_g.collidepoint(i.pos):
                        texture = All_textures["easy"]
                        print("easy")
                        start_screen = False
                        Green_Hill()
                elif start_screen == 4:
                    if start_g.collidepoint(i.pos):
                        texture = All_textures["normal"]
                        print("normal")
                        start_screen = False
                        Green_Hill()
                elif start_screen == 5:
                    if start_g.collidepoint(i.pos):
                        texture = All_textures["hard"]
                        print("hard")
                        start_screen = False
                        Green_Hill()
                elif start_screen == 6:
                    if start_g.collidepoint(i.pos):
                        texture = All_textures["madness"]
                        print("madness")
                        start_screen = False
                        Green_Hill()
               #elif finish == 2 and back_G.collidepoint(i.pos):
               #    start_screen = 1
               #    finish = 0
                
    for bad in bad_rects:
        if player.colliderect(bad):
            player.x = 35
            player.y = 0
    for good in good_rects:
        if player.colliderect(good):
            screen.blit(bg, (0, 0))
            screen.blit(end, (950, 460))
            screen.blit(back, (55, 460))
            if finish == 0:
                finish = 1
            elif finish == 1:
                finish = 2
            if finish == 1:
              pygame.mixer.music.pause()
              pygame.mixer.music.load(music_E)
              pygame.mixer.music.play()

    if finish != 2:
        if go_R == True:
            character = ch_R
            if player.width + movie < SCREEN_WIDTH:
                player.x += movie
        elif go_L == True:
            character = ch_L
            if player.x - movie > 0:
                player.x -= movie
        elif go_UP == True:
            if player.y - movie > 0:
                player.y -= movie
        elif go_D == True:
            if player.y + player.height + movie < SCREEN_HEIGHT:
                player.y += movie


    if start_screen == 2:
        screen.blit(tutarial, (0,0))
        screen.blit(title, title_coordinnate)
        screen.blit(easy_S, easy_coordinnate)
        screen.blit(normal_S, normal_coordinnate)
        screen.blit(hard_S, hard_coordinnate)
        screen.blit(madness_S, madness_coordinnate)

    elif start_screen == 3:
        y_S = 35
        screen.blit(easy, (0,0))
        for i in range(0, 3):
            info = font_little.render(info_about_modes["Easy"][str(i)], True, (0, 0, 0))
            screen.blit(info, (40, y_S))
            y_S += 50
        screen.blit(back, (55, 460))
        screen.blit(start, (900, 460))
    elif start_screen == 4:
        y_S = 35
        screen.blit(normal, (0,0))
        for i in range(0, 3):
            info = font_little.render(info_about_modes["Normal"][str(i)], True, (0, 0, 0))
            screen.blit(info, (40, y_S))
            y_S += 50
        screen.blit(back, (55, 460))
        screen.blit(start, (900, 460))
    elif start_screen == 5:
        y_S = 35
        screen.blit(hard, (0,0))
        for i in range(0, 3):
            info = font_little.render(info_about_modes["Hard"][str(i)], True, (0, 0, 0))
            screen.blit(info, (40, y_S))
            y_S += 50
        screen.blit(back, (55, 460))
        screen.blit(start, (900, 460))
    elif start_screen == 6:
        y_S = 35
        screen.blit(madness, (0,0))
        for i in range(0, 3):
            info = font_little.render(info_about_modes["Madness"][str(i)], True, (0, 0, 0))
            screen.blit(info, (40, y_S))
            y_S += 50
        screen.blit(back, (55, 460))
        screen.blit(start, (900, 460))

    pygame.display.flip()
    clock_game.tick(60)


