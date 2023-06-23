import time

import flet as ft
import requests as rq
import bs4 as bs

def main(page: ft.Page):
    page.title = "Парсер кинотеатра Гипопо"
    page.scroll = "AUTO"
    page.window_center()
    page.window_maximizable = False
    page.window_resizable = False
    page.window_width = 1280
    page.window_height = 720
    urlMovie = "http://xn--c1aksadab.xn--p1ai/kinoteatr/"
    movieText = ft.Text(value="Data: ")
    def parseMovie(e):
        req = rq.get(url=urlMovie)
        soup = bs.BeautifulSoup(req.text, features="html.parser")
        result = soup.find(name="tbody").find_all(name="span")
        movieText.value = f"Data:\n{result}"
        page.update()
    updateBtn = ft.ElevatedButton(text="Update", on_click=parseMovie)
    page.add(movieText, updateBtn)
    page.update()
    pass

ft.app(target=main)