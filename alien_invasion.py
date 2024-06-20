import sys
import pygame

class AlienInvasion:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Alien Invasion")
    
    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            
            pygame.display.flip()

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()

def __init__(self):

    pygame. display.set_caption("Alien Invasion")

# Set the background color.
    self.bg_color = (230, 230, 230)

def run_game(self):

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()



# Redraw the screen during each pass through the loop.
    self.screen.fill(self.bg_color)

# Make the most recently drawn screen visible.
    pygame.display.flip()