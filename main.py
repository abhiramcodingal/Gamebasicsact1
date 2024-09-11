import pygame

pygame.init()
screen = pygame.display.set_mode((300,400))

done = False
colour = (50,94,189)
rectangle = pygame.Rect(70, 70, 50, 60)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    screen.fill((255,255,0))
    pygame.draw.rect(screen, colour, rectangle)
    pygame.display.flip()

pygame.quit()