import pygame
import sys
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import Shot
def main():
    pygame.init()
    print("Starting Asteroids!")
    print(SCREEN_WIDTH)
    print(SCREEN_HEIGHT)
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    player = Player(x, y)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    asteroid_field = AsteroidField()
    Shot.containers = (shots, updatable, drawable)

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    # game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
                    
        screen.fill("black")
        for obj in drawable:
            obj.draw(screen)

        dt = clock.tick(60) / 1000
        for update in updatable:
            update.update(dt)

        for asteroid in asteroids:
            if player.collision_check(asteroid):
                print("Game over!")
                sys.exit()
            for shot in shots:
                if asteroid.collision_check(shot):
                    shot.kill()
                    asteroid.split()

        pygame.display.flip()
        
        
        


if __name__ == "__main__":
    main()