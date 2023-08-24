# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 00:28:41 2021

@author: thefi
"""

import pygame
import os
pygame.mixer.init()
pygame.font.init()

#pygame.mixer.music.load(os.path.join('Pew.mp3'))

WIDTH, HEIGHT = 1000, 600

WIN = pygame.display.set_mode ((WIDTH, HEIGHT))

pygame.display.set_caption('David vs Goliath')




BGCOLOR = (120, 120, 120)

BORDERCOLOR = (10, 10, 10)

health_font = pygame.font.SysFont("Helvetica", 40)

winner_font = pygame.font.SysFont('Times', 80)

RED = (220, 0, 0)

BLUE = (0, 0, 220)

BLACK = (0,0,0)

BORDER = pygame.Rect(WIDTH//2 - .5, 0, 1, HEIGHT)

FPS = 60

player1hit = pygame.USEREVENT + 1

player2hit = pygame.USEREVENT + 2


SQUAREVEL = 2.5

TRIANGLEVEL = 5

SQUARESPRINT = 5

TRIANGLESPRINT = 7.5


BULLETVEL = 10

MAXBULLETS = 5

SHAPE_WIDTH, SHAPE_HEIGHT = (50, 50)

RED_SQUARE_IMAGE = pygame.image.load(os.path.join('redsquare.png'))
RED_SQUARE = pygame.transform.scale(RED_SQUARE_IMAGE, (SHAPE_WIDTH, SHAPE_HEIGHT))

BLUE_TRIANGLE_IMAGE = pygame.image.load(os.path.join('bluetriangle.png'))
BLUE_TRIANGLE = pygame.transform.rotate(pygame.transform.scale(BLUE_TRIANGLE_IMAGE, (SHAPE_WIDTH, SHAPE_HEIGHT)), 90)


def draw_window(player1, player2, player1bullets, player2bullets, player1hp, player2hp):
    WIN.fill(BGCOLOR)
    pygame.draw.rect(WIN, BORDERCOLOR, BORDER)
    
    player1hptext = health_font.render("David HP: " + str (player1hp), 1, BLACK)
    
    player2hptext = health_font.render("Goliath HP: " + str(player2hp), 1, BLACK)
    WIN.blit(player1hptext, (50, 50))
    WIN.blit(player2hptext, (700, 50))
    
    #missiontext = ('Square is stronger, Triangle is faster. Kill or be killed!', 1, BLACK)
    
    
    WIN.blit(RED_SQUARE, (player1.x, player1.y))
    WIN.blit(BLUE_TRIANGLE, (player2.x, player2.y))
    
    
    
    for bullet in player1bullets:
        pygame.draw.rect(WIN, RED, bullet)
        
    for bullet in player2bullets:
        pygame.draw.rect(WIN, BLUE, bullet)
        
    pygame.display.update()
                
def player1movement(keys, player1): #Square
    key = pygame.key.get_pressed()
    if key[pygame.K_w] and player1.y > SQUAREVEL: # UP
        player1.y -= SQUAREVEL
        if key[pygame.K_LSHIFT]:
            player1.y -= SQUARESPRINT
    if key[pygame.K_s] and player1.y < HEIGHT - SHAPE_HEIGHT:
        player1.y += SQUAREVEL
        if key[pygame.K_LSHIFT]:
            player1.y += SQUARESPRINT
    if key[pygame.K_a] and player1.x - SQUAREVEL > 0:
        player1.x -= SQUAREVEL
        if key[pygame.K_LSHIFT]:
            player1.x -= SQUARESPRINT
    if key[pygame.K_d] and player1.x + SQUAREVEL + player1.width < BORDER.x:
        player1.x += SQUAREVEL
        if key[pygame.K_LSHIFT]:
            player1.x += SQUARESPRINT

def player2movement(keys, player2): #Triangle
    key = pygame.key.get_pressed()
    if key[pygame.K_UP] and player2.y > TRIANGLEVEL: # UP
        player2.y -= TRIANGLEVEL
        if key[pygame.K_RSHIFT]:
            player2.y -= TRIANGLESPRINT
    if key[pygame.K_DOWN] and player2.y < HEIGHT - SHAPE_HEIGHT:
        player2.y += TRIANGLEVEL
        if key[pygame.K_RSHIFT]:
            player2.y += TRIANGLESPRINT
    if key[pygame.K_LEFT] and player2.x + TRIANGLEVEL > BORDER.x :
        player2.x -= TRIANGLEVEL
        if key[pygame.K_RSHIFT]:
            player2.x -= TRIANGLESPRINT
    if key[pygame.K_RIGHT] and player2.x + SHAPE_WIDTH < WIDTH:
        player2.x += TRIANGLEVEL
        if key[pygame.K_RSHIFT]:
            player2.x += TRIANGLESPRINT
            
def handlebullets(player1bullets, player2bullets, player1, player2):
    for bullet in player1bullets:
        bullet.x += BULLETVEL
        if player2.colliderect(bullet):
            pygame.event.post(pygame.event.Event(player2hit)) #Is Player2 hit?
            player1bullets.remove(bullet)
        elif bullet.x > WIDTH:
            player1bullets.remove(bullet)
            
    for bullet in player2bullets:
        bullet.x -= BULLETVEL
        if player1.colliderect(bullet):
            pygame.event.post(pygame.event.Event(player1hit)) #Is Player1 hit?
            player2bullets.remove(bullet)
        elif bullet.x < 0:
            player2bullets.remove(bullet) 
            
def winner(text):
    draw_text = winner_font.render(text, 1, BLACK)
    WIN.blit(draw_text, (WIDTH//2 - draw_text.get_width()/2, HEIGHT//2 - draw_text.get_height()/2))
    pygame.display.update()
    pygame.time.delay(5000)
    
    

def game():
    player1 = pygame.Rect(100, 300, SHAPE_WIDTH, SHAPE_HEIGHT)
    player2 = pygame.Rect(900, 300, SHAPE_WIDTH, SHAPE_HEIGHT)
    
    player1bullets = []
    
    player2bullets = []
    
    player1hp = 15

    player2hp = 10
    
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                
            if event.type == pygame.KEYDOWN and len(player1bullets) < MAXBULLETS:
                if event.key == pygame.K_q:
                    bullet = pygame.Rect(player1.x + player1.width, player1.y + player1.height//2 - 2, 10, 5)
                    player1bullets.append(bullet)
                    #pygame.mixer.music.play()
                    
                if event.key == pygame.K_SLASH and len(player2bullets) < MAXBULLETS:
                    bullet = pygame.Rect(player2.x, player2.y + player2.height//2 - 2, 10, 5)
                    player2bullets.append(bullet)
                    
            if event.type == player1hit:
                player1hp -= 1
                
            if event.type == player2hit:
                player2hp -= 1
                
        winner_text = ''
        if player1hp <= 0:
            winner_text = "David Wins!"
            
        if player2hp <= 0:
            winner_text = "Goliath Wins!"
            
        if winner_text != '':
            winner(winner_text)
            break
        
        print(player1bullets, player2bullets)
        keys = pygame.key.get_pressed()
        
        player1movement(keys, player1)
        player2movement(keys, player2)
        
        handlebullets(player1bullets, player2bullets, player1, player2)
        
                
        draw_window(player1, player2, player1bullets, player2bullets, player1hp, player2hp)
game()