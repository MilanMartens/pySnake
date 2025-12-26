import pygame
from .Grid import Grid

class Snake:
    def __init__(
        self,
        x: float,
        y: float ,
        velocity_x: float,
        velocity_y: float,
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