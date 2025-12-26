import pygame

class Grid:
    def __init__(
        self,
        width:int,
        height:int,
        columns: int,
        column_kleur: tuple[int,int,int]
        ) -> None:
        
        self.width= width
        self.height = height
        self.columns = columns
        
        self.kolom_breedte = self.width / self.columns
        self.kolom_breedter_remainder = self.width % self.columns
        
        self.kolom_hoogte = self.height / self.columns
        self.kolom_hoogte_remainder = self.height % self.columns
        
        self.column_kleur = column_kleur
        
    def draw_vertical_lines(
        self,
        surface: pygame.Surface,
        boven_kant_scherm: int)-> None:
        
        for aantal in range(self.columns + 1):
            breedte = (self.kolom_breedte + self.kolom_breedter_remainder) * aantal
            if breedte > self.width:
                break
            rect = pygame.Rect(breedte, boven_kant_scherm, 1, self.height)
            pygame.draw.rect(surface, self.column_kleur, rect)
            
    def draw_horizontal_lines(
        self,
        surface: pygame.Surface,
        linker_zijkant:int
        )-> None:
        
        for aantal in range(self.columns + 1):
            height = (self.kolom_hoogte + self.kolom_hoogte_remainder) * aantal
            if height > self.height:
                break
            rect = pygame.Rect(linker_zijkant, height, self.width, 1)
            pygame.draw.rect(surface, self.column_kleur, rect)
        
        
    def draw_grid(
        self,
        surface: pygame.Surface,
        )-> None: 
        
        boven_kant_scherm = 0
        linker_zijkant = 0
        self.draw_vertical_lines(surface, boven_kant_scherm)
        self.draw_horizontal_lines(surface, linker_zijkant)
        
    def redraw_grid(self, surface, zwart):
        surface.fill(zwart)
        self.draw_grid(surface)