import nltk

from gui.Window import *
from gui.Button import *
from gui.Colors import *
from gui.Constant import *
from gui.Cursor import *
from gui.İmage import *
from gui.ListMenu import *
from gui.Text import *
from gui.Textbox import *

from func import *

import time
import sys

pg.font.init()
pg.init()

Font = pg.font.SysFont("consolas", 18, False)

Screen = Window(500, 700, "test", 30)
Cursor = Cursor(Screen.Window)
Text_input = Text_box(Screen, 30, 615, 300, 70, Cursor, Font_size=16, Font_name="Verdana")
Sumbit_button = Button(Screen, Cursor, 350, 615, 35, 90, Up_Maroon, Text="Sumbit")
Title_1 = uneditable_Text(Screen, 10, 10, "Chatbot", 20, "Times New Roman")

response_1 = ""
response = ""
Raw_response = ""
Bot_response = ""
response_Y = 500

User_responses_object = []
Bot_responses_object = []

User_response_slices = []
Bot_response_slices = []

flag = True
send_response = False
while flag:
    sayac_1 = 0
    User_response_text_border = pg.draw.rect(Screen.Window, Green, (255, 0, 240, 600), 1)
    Bot_response_text_border = pg.draw.rect(Screen.Window, Green, (5, 0, 240, 600), 1)

    Cursor.Draw()
    Screen.Window.fill(Alabaster)

    pg.draw.rect(Screen.Window, Desert_Sand, (250, 0, 250, 700))
    pg.draw.rect(Screen.Window, Flame, (0, 600, 500, 100))

    Text_input.Draw()
    Sumbit_button.Draw(Color=Black, Font_name="Verdana")

    Key = pg.key.get_pressed()

    for event in Get():
        Text_input.Type(event)

        if event.type == pg.QUIT:
            sys.exit()

        if Sumbit_button.Collide(event) or (Key[K_KP_ENTER]):
            # Kullanıcının gireceği cevabın pixel cinsinden uzunluğu eğer belirlenen sınırdan uzunsa, cevap parçalara
            # bölünüp tek tek "User_response_slices" değişkeninde saklanır

            sayac = 0
            response_1 = ""
            Raw_response = ""

            Raw_response = f"YOU :.. {Text_input.Get_Text()}"

            if Raw_response != "":
                send_response = True

                if Font.size(Raw_response)[0] >= User_response_text_border.width:

                    for i in Raw_response:
                        response_1 += i

                        if Font.size(response_1)[0] >= User_response_text_border.width:
                            sayac += 1
                            User_response_slices.append(response_1)
                            response_1 = ""
                            Text_input.Delete()

                if sayac == len(User_response_slices):
                    User_response_slices.append(response_1)
                    Text_input.Delete()
                    response_1 = ""

                if sayac == 0:
                    User_response_slices.append(Raw_response)
                    Text_input.Delete()

            # Cevap objelerinin pozisyonlarının yenilendiği blok (Bir mesaj yazıldığı zaman ekrandaki yazıların yukarı doğru akması)
            if Raw_response != "":
                for i in User_responses_object:
                    i.Y -= 30

            if Bot_response != "":
                for i in Bot_responses_object:
                    i.Y -= 30

    if len(User_responses_object) != len(User_response_slices) or len(User_responses_object) == len(
            User_response_slices):
        sayac = 0
        for i in User_response_slices:

            Text = uneditable_Text(Screen, 260, response_Y, User_response_slices[sayac], Font_name="Verdana")
            User_responses_object.append(Text)
            User_response_slices.remove(User_response_slices[sayac])
            sayac + 1

            if len(User_response_slices) >= 1:
                for j in User_responses_object:
                    j.Y -= 15

        response_Y = 500

    if len(Bot_responses_object) != len(Bot_response_slices) or len(Bot_responses_object) == len(Bot_response_slices):
        sayac_1 = 0
        for i in Bot_response_slices:

            Text = uneditable_Text(Screen, 20, response_Y, Bot_response_slices[sayac], Font_name="Verdana")
            Bot_responses_object.append(Text)
            Bot_response_slices.remove(Bot_response_slices[sayac])
            sayac_1 + 1

            if len(Bot_response_slices) >= 1:
                for j in Bot_responses_object:
                    j.Y -= 15

        response_Y = 500

    # konuşmanın ekranda görsetirldiği kısım
    for i in User_responses_object:
        i.Draw()

    for i in Bot_responses_object:
        i.Draw()
    # -------------------------------------

    pg.draw.rect(Screen.Window, Atomic_Tangerine, (0, 0, 500, 40))
    pg.draw.rect(Screen.Window, Black, (-30, -10, 600, 50), 2)
    Title_1.Draw()

    # Kosinüs benzerliğine bakılarak cevapların saklandığı kısım
    if send_response:

        Raw_response = Raw_response.lower()
        response = ""

        if Raw_response == 'bye' or Raw_response == 'thank you' or Raw_response == 'thankyou' or Raw_response == "thanks":
            Update()
            time.sleep(2)

        else:
            if greeting(Raw_response) != None:
                Bot_response = f"BOT :.. {greeting(Raw_response)}"
                send_response = False

            else:
                sent_tokens.append(Raw_response)
                word_tokens = word_tokens + nltk.word_tokenize(Raw_response)
                final_words = list(set(word_tokens))
                Bot_response = f"BOT :.. {Response()}"
                sent_tokens.remove(Raw_response)
                send_response = False

        # Programın döndüreceği cevabın pixel cinsinden uzunluğu eğer belirlenen sınırdan uzunsa, cevap parçalara
        # bölünüp tek tek "Bot_response_slices" değişkeninde saklanır
        if Bot_response != "":
            if Font.size(Bot_response)[0] >= Bot_response_text_border.width:
                for i in Bot_response:
                    response += i

                    if Font.size(response)[0] >= Bot_response_text_border.width:
                        sayac_1 += 1
                        Bot_response_slices.append(response)
                        response = ""
            if sayac_1 == 0:
                Bot_response_slices.append(Bot_response)

            if sayac_1 == len(Bot_response_slices):
                Bot_response_slices.append(response)
                response = ""

    # Fare imlecinin posizyonunun alındığı fonksiyon
    Cursor.Get_pos()
    # Görüntünü  tazelendiği fonksiyon
    Update()




# Benim hayattaki yegane fahrim, servetim Türklükten başka bir şey değildir !
#
#                                               -- Mustafa Kemal ATATÜRK