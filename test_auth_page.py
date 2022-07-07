from pages.auth_page import AuthPage
import time
import pytest


def test_auth_page(selenium):
   page = AuthPage(selenium)
   page.enter_email("ok.bre@inbox.lv")
   page.enter_pass("beredisa")
   page.btn_click()

   #знак != или == будет зависеть от того, верные или неверные данные мы вводим
   assert page.get_relative_link() != '/all_pets', "login error"

   time.sleep(5) #задержка для учебных целей

# py -m pytest -v --driver Chrome --driver-path chromedriver.exe test_auth_page.py
# - путь для теста

