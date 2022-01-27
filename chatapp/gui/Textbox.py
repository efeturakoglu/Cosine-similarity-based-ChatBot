import pygame as pg
from pygame.constants import MOUSEBUTTONDOWN
from gui.Colors import *

class Text_box:
    def __init__(self, Window, X, Y, Width, Heigth, Cursor, Font_name = "consolas", Font_size = 20, Color = Black) -> None:

        self.X = X
        self.Y = Y

        self.Width = Width
        self.Heigth = Heigth

        self.Window = Window
        self.Cursor = Cursor

        self.Active = False
        self.Active1 = True

        self.Text_list = []
        self.Text = ""
        self.Text_2 = ""
        self.Line_number = int(self.Heigth / Font_size)
        self.Font_name = Font_name

        self.Font_size = Font_size
        self. Color = Color


    def Type(self, event):

        # Dedect collide and typing
        if event.type == MOUSEBUTTONDOWN:
            if self.Rect.colliderect(self.Cursor.Cursor):
                self.Active = True
            else:
                self.Active = False

        if self.Active:
            if event.type == pg.KEYDOWN:
                
                # Delete text
                if event.key == pg.K_BACKSPACE:
                    if self.Text == "":
                        self.Text_list=self.Text_list[:-1]

                    else:
                        self.Text = self.Text[:-1]


                # Type text
                else:
                    if self.Active1:
                        self.Text += event.unicode

    def Draw(self):
        # Draw Text_box and Text
        self.Rect = pg.draw.rect(self.Window.Window,Black,(self.X, self.Y, self.Width, self.Heigth),1)

        Font = pg.font.SysFont(self.Font_name, self.Font_size, False)
        text_y = self.Y

        # text slices saving in the Text_list
        if Font.size(self.Text)[0] >= self.Width - self.Font_size:
            self.Text_list.append(self.Text)
            self.Text = ""

        #after step, draw inputs in screen
        if self.Text_list == []:
            self.Window.Window.blit(Font.render(self.Text, True, self.Color), (self.X + 5, text_y))

        else:
            for i in self.Text_list:
                self.Window.Window.blit(Font.render(i,True,self.Color), (self.X + 5, text_y))
                text_y += Font.size(i)[1]

            if len(self.Text_list) >= 1:
                self.Window.Window.blit(Font.render(self.Text, True, self.Color), (self.X + 5, text_y))

            if len(self.Text_list) == self.Line_number:
                self.Active1 = False

    def Get_Text(self):

        self.Text_2 = ""
        if self.Text_list == []:
            return self.Text
        else:
            for i in self.Text_list:
                self.Text_2 += i
            self.Text_2 += self.Text
            return self.Text_2


    def Delete(self):
        self.Text = ""
        self.Text_list = []
        self.Text_2 = ""
        self.Active1 = True

