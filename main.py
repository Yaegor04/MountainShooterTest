import pygame

pygame.init()
print('Setup Start')
window = pygame.display.set_mode(size=(800, 680))
print('Setup End')

print('Loop Start')
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()