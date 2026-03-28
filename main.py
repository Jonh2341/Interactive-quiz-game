import pygame

pygame.init()

screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption('My game')

questions = [
    {"question": "What is 2 + 2?", "options": ["22", "4", "2"], "answer": 1},
    {"question": "Capital of France?", "options": ["Berlin", "Geneva", "Paris"], "answer": 1},
]

current_question = 0
score = 0

def draw_question():
    screen.fill((20, 20, 20))
        

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