
import pygame as pg



pg.init()
pg.font.init()

class Window:
    def __init__(self,x,y,Name= "test",Fps = 5) -> None:
        self.Window = pg.display.set_mode((x,y))
        pg.display.set_caption(Name)
        self.Fps = Fps
        self.Clock = pg.time.Clock()

def Update():

    return pg.display.update()

        

    

