import pygame
from .Grid import Grid

class Snake:
    def __init__(
        self,
        x: float,
        y: float ,
        velocity_x: int,
        velocity_y: int,
        head_color: tuple[int,int,int],
        body_color: tuple[int,int,int],
        grid: Grid
        ) -> None:  
        
        self.x = x
        self.y = y
        
        # GAAN WE NAAR LINKS OF RECHTS
        self.velocity_x = velocity_x
        # GAAN WE NAAR BOVEN OF ONDER
        self.velocity_y = velocity_y
        
        self.lengte = grid.kolom_hoogte + grid.kolom_hoogte_remainder
        self.breedte = grid.kolom_breedte + grid.kolom_breedter_remainder
        
        self.grid = grid
        self.head_color = head_color
        self.body_color = body_color
        
        
    def draw_snake_head(
        self,
        surface: pygame.Surface,
        ) -> None:
        
        hoofd_slang: pygame.Rect = pygame.Rect(self.x, self.y, self.breedte, self.lengte)
        pygame.draw.rect(surface, self.head_color, hoofd_slang)
        
    def go_right(
        self,
        surface: pygame.Surface,
        zwart: tuple[int,int,int] = (0, 0, 0)
        )-> None:
        
        self.grid.redraw_grid(surface, zwart)   
        self.velocity_x = -1
        self.velocity_y = 0     
        self.x += self.breedte
        self.draw_snake_head(surface)


    def go_left(
        self,
        surface: pygame.Surface,
        zwart: tuple[int,int,int] = (0, 0, 0)
        )-> None:
        
        self.grid.redraw_grid(surface, zwart)
        self.velocity_x = 1
        self.velocity_y = 0             
        self.x -= self.breedte
        self.draw_snake_head(surface)
    
    def go_up(
        self,
        surface: pygame.Surface,
        zwart: tuple[int,int,int] = (0, 0, 0)
        )-> None:
        self.grid.redraw_grid(surface, zwart)  
        self.velocity_x = 0
        self.velocity_y = -1            
        self.y -= self.lengte
        self.draw_snake_head(surface)
        
        
    def go_down(
        self,
        surface: pygame.Surface,
        zwart: tuple[int,int,int] = (0, 0, 0)
        )-> None:
        self.grid.redraw_grid(surface, zwart) 
        self.velocity_x = 0
        self.velocity_y = 1        
        self.y += self.lengte
        self.draw_snake_head(surface)
        
    def move_in_direction(
        self, 
        surface: pygame.Surface,
        grid: Grid
    )-> None:
        DIRECTION_MAP = {
            (0, -1): self.go_right,
            (0, 1): self.go_left,
            (1, 0): self.go_down,
            (-1, 0): self.go_up
        }
        self.check_for_game_over(grid)
        
        richting = DIRECTION_MAP.get((self.velocity_y, self.velocity_x))
        if richting:
            richting(surface)
            

    def check_for_game_over(
        self,
        grid: Grid
        )-> None:
        if self.not_on_screen(grid):
            print("GAME OVER")
            pygame.quit()
            quit()

    def not_on_screen(self, grid):
        return (self.x + 50 >= grid.width) or (self.x - 50 < 0) or (self.y - 50 < 0) or (self.y + 50 >= grid.height)
            
    