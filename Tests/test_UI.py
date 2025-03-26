from selenium import webdriver
import allure
import pytest
from pages.search import search
from specific_data import UI_URL, cyrillic, latin, digit, specific_symbols, search_phrase

chromeDriver = webdriver.Chrome()
mainPage = search(chromeDriver, UI_URL)


@allure.title('Строка поиска принимает ввод на кириллице')
@allure.description('')
@allure.feature('Поиск')
@allure.severity('S3')
@pytest.mark.UI
def test_search_cyrillic_input_positive():
    with allure.step('Открыть главную страницу'):
        mainPage.open()
    with allure.step('Ввести в строку поиска символы на кириллице'):
        mainPage.search_input(cyrillic)
    with allure.step('Введенные символы должны отобразиться в строке поиска'):
        assert mainPage.get_search_bar_content() == cyrillic


@allure.title('Строка поиска принимает ввод на латинице')
@allure.description('')
@allure.feature('Поиск')
@allure.severity('S3')
@pytest.mark.UI
def test_search_latin_input_positive():
    with allure.step('Открыть главную страницу'):
        mainPage.open()
    with allure.step('Ввести в строку поиска символы на латинице'):
        mainPage.search_input(latin)
    with allure.step('Введенные символы должны отобразиться в строке поиска'):
        assert mainPage.get_search_bar_content() == latin


@allure.title('Строка поиска принимает ввод цифрами')
@allure.description('')
@allure.feature('Поиск')
@allure.severity('S3')
@pytest.mark.UI
def test_search_digit_input_positive():
    with allure.step('Открыть главную страницу'):
        mainPage.open()
    with allure.step('Ввести в строку поиска цифры'):
        mainPage.search_input(digit)
    with allure.step('Введенные символы должны отобразиться в строке поиска'):
        assert mainPage.get_search_bar_content() == digit


@allure.title('Строка поиска принимает ввод спецсимволами')
@allure.description('')
@allure.feature('Поиск')
@allure.severity('S3')
@pytest.mark.UI
def test_search_special_signs_input_positive():
    with allure.step('Открыть главную страницу'):
        mainPage.open()
    with allure.step('Ввести в строку поиска спецсимволы'):
        mainPage.search_input(specific_symbols)
    with allure.step('Введенные символы должны отобразиться в строке поиска'):
        assert mainPage.get_search_bar_content() == specific_symbols


@allure.title('Производится поиск при нажатии кнопки поиск с введенными цифрами в строке поиска')
@allure.description('')
@allure.feature('Поиск')
@allure.severity('S3')
@pytest.mark.UI
def test_search_button_positive():
    with allure.step('Открыть главную страницу'):
        mainPage.open()
    with allure.step('Ввести в строку поиска поисковый запрос'):
        mainPage.search_input(digit)
    with allure.step('Нажать кнопку поиска'):
        mainPage.search_button_click()
    with allure.step('Откроется страница с результатами поиска по указанному запросу'):
        assert chromeDriver.current_url == UI_URL + search_phrase + digit
