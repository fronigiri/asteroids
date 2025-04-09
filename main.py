import pygame
from constants import *
from player import *
def main():
    pygame.init()
    print("Starting Asteroids!")
    print(SCREEN_WIDTH)
    print(SCREEN_HEIGHT)
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player = Player(x, y)

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    # game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return        
        screen.fill((0,0,0))
        player.draw(screen)
        dt = clock.tick(60) / 1000
        player.update(dt)
        pygame.display.flip()
        
        
        


if __name__ == "__main__":
    main()