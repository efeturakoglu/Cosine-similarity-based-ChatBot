import bs4 as bs
import urllib.request
from urllib.parse import quote

import os


a = os.getcwd()
print(a)


text = ""

src_1 = urllib.request.urlopen(
    f'file:///{a}\\sources_en\\Biography%20of%20Atat%C3%BCrk.html',
    "utf-8").read()
src_2 = urllib.request.urlopen(
    f'file:///{a}/sources_en/Kemal%20Ataturk%20_%20Biography,%20Reforms,%20Death,%20&%20Facts%20_%20Britannica.html',
    "utf-8").read()
src_3 = urllib.request.urlopen(
    f'file:///{a}/sources_en/Mustafa%20Kemal%20Atat%C3%BCrk%20-%20Wikipedia.html',
    "utf-8").read()
src_4 = urllib.request.urlopen(
    f'file:///{a}/sources_en/Presidency%20Of%20The%20Republic%20Of%20Turkey%20_%20Biography.html',
    "utf-8").read()
src_5 = urllib.request.urlopen(
    f'file:///{a}/sources_en/Turkish%20Military%20Academy.html',
    "utf-8").read()



material_1 = bs.BeautifulSoup(src_1, "html.parser")
print("+")
material_2 = bs.BeautifulSoup(src_2, "html.parser")
print("+")
material_3 = bs.BeautifulSoup(src_3, "html.parser")
print("+")
material_4 = bs.BeautifulSoup(src_4, "html.parser")
print("+")
material_5 = bs.BeautifulSoup(src_5, "html.parser")
print("+")


soup = [material_1, material_2, material_3, material_4, material_5]

for m in soup:
    for paragraph in m.find_all('p'):
        text += paragraph.text

raw = text.lower()
