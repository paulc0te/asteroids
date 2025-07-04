import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

# Creating sprite groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

# Containing objects to sprite goups
    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()

    Player.containers = (updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    dt = 0

# Game loop
    while True:
# Reaction for ctrl+c
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

# Update all objects
        updatable.update(dt)

# Check collides asteroids with player
        for asteroid in asteroids:
            if asteroid.collides_with(player):
                print("Game over!")
                sys.exit()
# Check collides asteroids with bullets
            for shot in shots:
                if asteroid.collides_with(shot):
                    shot.kill()     # kill object
                    asteroid.split()


# Coloring Screen
        screen.fill("black")

# Draw all objects
        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()

        # limit the framerate to 60 FPS
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
