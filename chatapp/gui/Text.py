import pygame as pg

Black = (0,0,0)

pg.font.init()

class uneditable_Text:
    def __init__(self, Window, X = 0, Y = 0, text = "None",Font_size = 12, Font_name = "consolas", Color = Black) -> None:


        self.Text = text
        self.X = X
        self.Y = Y
        self.Window = Window
        self.Font = pg.font.SysFont(Font_name,Font_size,False)
        self.Text_render = self.Font.render(text, True, Color)


    def Draw(self):
        self.Window.Window.blit(self.Text_render, (self.X,self.Y))
