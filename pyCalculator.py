import pygame
import random
import math

pygame.init()
background = pygame.image.load("circle.png")
screen = pygame.display.set_mode((750, 750))
pygame.display.set_caption("calculator")
pointsImg = []

pointsX = []
pointsY = []
pointIn = 0
pointOut = 0


def point(x, y, p):
    screen.blit(pointsImg[p], (x, y))


font = pygame.font.Font("freesansbold.ttf", 30)
textX = 0
textY = 0


def value(X, Y, num):
    over_text = font.render(str(float(num)), True, (255, 100, 70))
    screen.blit(over_text, (X, Y))



counter = 0

running = True
while running:
    screen.fill((255, 255, 255))
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pointsX.append(random.uniform(0, 750))
    pointsY.append(random.uniform(0, 750))
    pointsImg.append(pygame.image.load('point.png'))
    counter += 1
    if math.pow(pointsX[-1], 2) + math.pow(pointsY[-1], 2) < math.pow(750, 2):
        pointIn += 1
    elif math.pow(pointsX[-1], 2) + math.pow(pointsY[-1], 2) > math.pow(750, 2):
        pointOut += 1

    for i in range(0, counter):
        point(pointsX[i], pointsY[i], i)

    value(textX, textY, float(4 * pointIn / (pointIn + pointOut)))
    pygame.display.update()


# System.out.println((double)4*counterIn/(counterIn+counterOut));
