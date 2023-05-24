#!/usr/bin/env python
# coding: utf-8

# In[7]:


import pygame
import random

pygame.init()

####################

width, height = 800, 600
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Bouncing Ball Game")

####################

ball_radius = 20
ball_color = (255, 0, 0)
ball_pos = [random.randint(ball_radius, width - ball_radius), random.randint(ball_radius, height - ball_radius)]
ball_speed = [random.randint(-1, 1), random.randint(-1, 1)]

####################

colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (0, 255, 255), (255, 0, 255)]
current_color_index = 0

####################

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    ball_pos[0] += ball_speed[0]
    ball_pos[1] += ball_speed[1]

    if ball_pos[0] <= ball_radius or ball_pos[0] >= width - ball_radius:
        ball_speed[0] = -ball_speed[0]
        ball_color = random.choice(colors)
    if ball_pos[1] <= ball_radius or ball_pos[1] >= height - ball_radius:
        ball_speed[1] = -ball_speed[1]
        ball_color = random.choice(colors)

    window.fill((0, 0, 0))

    pygame.draw.circle(window, ball_color, (ball_pos[0], ball_pos[1]), ball_radius)

    pygame.display.flip()


pygame.quit()

