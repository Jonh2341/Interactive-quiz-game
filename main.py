import pygame

pygame.init()

screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption('My game')

running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill('purple')

    # pygame.draw.rect(screen, "green", (100, 100, 200, 150))
    # pygame.draw.rect(screen, "green", (980, 100, 200, 150))
    # pygame.draw.rect(screen, "green", (550, 400, 200, 200))

    pygame.display.flip()

pygame.quit()