import pygame as pg
from pygame.constants import MOUSEBUTTONDOWN
from gui.Colors import *

pg.font.init()


class Selectable_Text_button:
    def __init__(self, X, Y, Text_color, i, Window, Color, Width, Font_size = 18, Font_name = "consolas"):
        self.Y = Y
        self.X = X
        self.Width = Width
        self.Font_size = Font_size
        self.Font_name = Font_name
        self.Window = Window
        self.Text_color = Text_color
        self.Color = Color
        self.Window = Window
        self.İtem = i
        self.Font = pg.font.SysFont(self.Font_name, self.Font_size, False)

    def Draw(self):

        self.Border = pg.draw.rect(self.Window.Window, self.Color, (self.X, self.Y, self.Width,self.Font.size(self.İtem)[1]))
        self.List_text_render = self.Font.render(self.İtem, True, self.Text_color)
        self.Window.Window.blit(self.List_text_render, (self.X, self.Y))


class List_menu:
    def __init__(self, Window, Cursor, X, Y, Width, Heigth, List=[], Color=(255, 255, 255), Text_color=Black,
                 Font_name="consolas", Font_size=18, Text=""):
        self.Cursor = Cursor
        self.Window = Window
        self.X = X
        self.Y = Y
        self.Color = Color
        self.Width = Width
        self.Heigth = Heigth
        self.Active = "Close"

        self.Button_text = Text
        self.Font_size = Font_size
        self.Font_name = Font_name
        self.Text_color = Text_color

        self.Button_list = []
        self.List = List

        X = self.X
        Y = self.Y + self.Heigth

        for i in self.List:
            a = Selectable_Text_button(X, Y, self.Text_color, i, self.Window, self.Color, self.Width,self.Font_size)
            self.Button_list.append(a)
            Y += a.Font.size(a.İtem)[1]

    def Draw(self):

        self.Border = pg.draw.rect(self.Window.Window, self.Color, (self.X, self.Y, self.Width, self.Heigth))

        Font = pg.font.SysFont(self.Font_name, self.Font_size, False)

        if Font.size(self.Button_text)[0] >= self.Width:
            self.Font_size -= 1

        self.Text_render = Font.render(self.Button_text, True, self.Text_color)
        self.Window.Window.blit(self.Text_render, (self.X, self.Y ))

        if self.Active == "Open":
            for i in self.Button_list:
                i.Draw()

    def Collide(self, event):

        if event.type == MOUSEBUTTONDOWN:
            if self.Active == "Open":
                for i in self.Button_list:
                    if i.Border.colliderect(self.Cursor.Cursor):
                        self.Button_text = i.İtem
                        self.Active = "Close"

            if not self.Border.colliderect(self.Cursor.Cursor):
                self.Active = "Close"
            else:
                if self.Active == "Close":
                    self.Active = "Open"
                else:
                    self.Active = "Close"

# Hiç bir zafer amaç değildir. Zafer, ancak kendisinden daha büyük bir amacı elde etmek için belli başlı bir vasıtadır !