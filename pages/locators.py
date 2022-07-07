from selenium.webdriver.common.by import By

class AuthLocators:
    AUTH_EMAIL = (By.ID, "email")
    AUTH_PASS = (By.ID, "pass")
    AUTH_BTN = (By.CLASS_NAME, "btn-success")

# Тут нам необходимо импортировать класс By, содержащий определения разных типов поиска.
# Далее мы внутри класса определяем локаторы в виде списка с типом поиска и поисковой фразой (строкой локатора).
