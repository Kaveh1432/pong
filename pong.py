import pygame
import sys

pygame.init()

# Set up the game window
size = width, height = 640, 480
black = 0, 0, 0
speed = [2, 2]

screen = pygame.display.set_mode(size)

# Create paddles and ball
paddle1 = pygame.Rect(30, 200, 10, 100)
paddle2 = pygame.Rect(600, 200, 10, 100)
ball = pygame.Rect(320, 240, 20, 20)
ball_speed = [2, 2]

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and paddle1.top > 0:
        paddle1.move_ip(0, -5)
    if keys[pygame.K_s] and paddle1.bottom < height:
        paddle1.move_ip(0, 5)
    if keys[pygame.K_UP] and paddle2.top > 0:
        paddle2.move_ip(0, -5)
    if keys[pygame.K_DOWN] and paddle2.bottom < height:
        paddle2.move_ip(0, 5)

    ball.move_ip(ball_speed)
    if ball.top <= 0 or ball.bottom >= height:
        ball_speed[1] = -ball_speed[1]
    if ball.colliderect(paddle1) or ball.colliderect(paddle2):
        ball_speed[0] = -ball_speed[0]

    screen.fill(black)
    pygame.draw.rect(screen, (255, 255, 255), paddle1)
    pygame.draw.rect(screen, (255, 255, 255), paddle2)
    pygame.draw.ellipse(screen, (255, 255, 255), ball)
    pygame.display.flip()
