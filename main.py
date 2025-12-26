import pygame
from Class import *
from helpFunc import *
# 
#   TODO ZORG DAT WE NIET SPRINGEN BIJ HET VERWISSELEN VAN RICHTING. 
# 

pygame.init()

HEIGHT = 600
WIDTH = 600
WIT = (255,255,255)
BLAUW = (0, 0, 255)
ROOD = (255,0,0)
AANTAL_KOLOMEN = 12

gameDisplay = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("SNAKE")

clock = pygame.time.Clock()

# MAAK HET GRID AAN.
grid = Grid(WIDTH, HEIGHT, AANTAL_KOLOMEN, WIT)
grid.draw_grid(gameDisplay)

# MAAK DE SLANG AAN
begin_lengte = 1
# GAAN WE NAAR BOVEN OF ONDER
snelheid_y = 0
# GAAN WE NAAR LINKS OF RECHTS
snelheid_x = -1

snake = Snake(WIDTH/2, HEIGHT/2 , snelheid_x, snelheid_y, BLAUW, ROOD, grid)
snake.draw_snake_head(gameDisplay)

DIRECTION_MAP = {
    (0, -1): snake.go_right,
    (0, 1): snake.go_left,
    (1, 0): snake.go_down,
    (-1, 0): snake.go_up
}

#TODO SPAWN EEN FRUITJE
# fruit = Fruit()

crashed = False
while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
            
        # als we rechter pijl induwen
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT and not over_x(snake.velocity_x):
                snake.go_right(gameDisplay)
                
            elif event.key == pygame.K_LEFT and not over_x(snake.velocity_x):
                snake.go_left(gameDisplay)
                
            elif event.key == pygame.K_UP and not over_y(snake.velocity_y):
                snake.go_up(gameDisplay)
                
            elif event.key == pygame.K_DOWN and not over_y(snake.velocity_y):
                snake.go_down(gameDisplay)
    
    func = DIRECTION_MAP.get((snake.velocity_y, snake.velocity_x))
    if func:
        func(gameDisplay)

    # refresh window  
    pygame.display.update()
    # 60fps
    clock.tick(3)

pygame.quit()
quit()