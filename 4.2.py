import pygame
from pygame.draw import *
import math
pygame.init()
w = 800
h = 800
FPS = 30
screen = pygame.display.set_mode((w, h))

# sky
polygon(screen, (100, 150, 255), [(0, 0), (w, 0),
                                  (w, h // 2), (0, h // 2),
                                  (0, 0)])
# grass
polygon(screen, (0, 255, 0), [(0, h // 2), (w, h // 2),
                                  (w, h), (0, h),
                                  (0, h // 2)])


def house(x, y, d):
    polygon(screen, (80, 50, 20), [(x, y), (x, y + d * 3 // 4),
                                      (x + d, y + d * 3 // 4), (x + d, y),
                                      (x, y)])
    polygon(screen, (255, 30, 30), [(x, y), (x + d, y),
                                      (x + d // 2, y - d // 2), (x, y)])
    polygon(screen, (80, 50, 200), [(x + d // 10 * 3, y + d // 4), (x + d // 10 * 3, y + d // 2),
                                  (x + d * 7 // 10, y + d // 2), (x + d * 7 // 10, y + d // 4),
                                  (x + d // 10 * 3, y + d // 4)])


def tree(x, y, r):
    polygon(screen, (0, 0, 0), [(x, y), (x + 2 * r // 5, y), (x + 2 * r // 5, y + 4 * r), (x, y + 4 * r), (x, y)])
    leaf(x + 7 * r // 5, y - r, r)
    leaf(x - r, y - r, r)
    leaf(x + r // 5, y - 9 * r // 5, r)
    leaf(x - r // 5, y + 2 * r // 5, r)
    leaf(x + 3 * r // 5, y + 2 * r // 5, r)
    leaf(x + r // 5, y - 2 * r // 5, r)

    
def leaf(x, y, r):
    circle(screen, (20, 150, 20), (x, y), r)
    circle(screen, (0, 0, 0), (x, y), r, 1)

    
def cloud(x, y, r):
    circle(screen, (255, 255, 255), (x, y), r)
    circle(screen, (0, 0, 0), (x, y), r, 1)

def group_of_clouds(x, y, r):
    cloud(x + 3 * r, y, r)
    cloud(x + 2 * r, y, r)
    cloud(x + r, y, r)
    cloud(x, y, r)
    cloud(x + r * 5 // 2, y - r, r)
    cloud(x + r * 3 // 2, y - r, r)
    
def sun(x, y, r):
    for i in range(37):
        c = i * math.pi / 36
        polygon(screen, (255, 100, 100),[(int(x + r * math.cos(c)), int(y - r * math.sin(c))),
     (int(x + r * math.cos(math.pi * 2 / 3 + c)), int(y - r * math.sin(math.pi * 2 / 3 + c))),
     (int(x + r * math.cos(math.pi * 4 / 3 + c)), int(y - r * math.sin(math.pi * 4 / 3 + c)))])


tree(200, 570, 25)
tree(700, 570, 35)
house(300, 450, 100)
house(500, 475, 70)   
group_of_clouds(90, 150, 20)
group_of_clouds(600, 200, 30)
sun(500, 200, 60)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
