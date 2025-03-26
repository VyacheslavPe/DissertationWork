from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

class search:
    def __init__(self, driver : WebDriver, UI_URL : str):
        self.UI_URL = UI_URL
        self._driver = driver
        self._driver.implicitly_wait(4)



    def open(self):
        """
        Открыть страницу и развернуть на весь экран
        """
        # открыть страницу
        self._driver.get(self.UI_URL)
        # развернуть на весь экран
        self._driver.maximize_window()


    def search(self, value : str):
        """
        Выполнить поиск по строке value
        """
        # найти поле ввода поиска
        self.search_bar = self._driver.find_element(By.CLASS_NAME, 'header-search__input')
        # найти кнопку поиска
        self.search_button = self._driver.find_element(By.CLASS_NAME, 'header-search__button')
        # очистить поле поиска
        self.search_bar.clear()
        # ввести значение value в строку поиска
        self.search_bar.send_keys(value)
        # нажать кнопку поиска
        self.search_button.click()


    def search_input(self, value : str):
        """
        Ввести в строку поиска значение value
        """
        # найти строку поиска
        self.search_bar = self._driver.find_element(By.CLASS_NAME, 'header-search__input')
        # очистить строку поиска
        self.search_bar.clear()
        # ввести значение value в строку поиска
        self.search_bar.send_keys(value)

    def search_button_click(self):
        """
        Нажать кнопку поиска
        """
        # найти кнопку поиска
        self.search_button = self._driver.find_element(By.CLASS_NAME, 'header-search__button')
        # нажать кнопку поиска
        self.search_button.click()

    def get_search_bar_content(self):
        """
        Получить содержимое строки поиска
        """
        # найти строку поиска
        self.search_bar = self._driver.find_element(By.CLASS_NAME, 'header-search__input')
        # получить параметр _value строки поиска и вернуть его
        return  self.search_bar.get_attribute('_value')

    def sort_new_first(self):
        """
        Отсортировать по новизне
        """
        # найти выпадающий список сортировки
        self.sort_dropdown = self._driver.find_element(By.CLASS_NAME, 'chg-app-custom-dropdown__label')
        # нажать на выпадающий список сортировки
        self.sort_dropdown.click()
        # в выпавшем списке найти все методы способы сортировки
        self.sort_dropdown_list = self._driver.find_elements(By.CLASS_NAME, 'chg-app-dropdown-custom-item')
        # нажать на второй элемент в выпавшем списке
        self.sort_dropdown_list[1].click()

    def sort_cheaper_first(self):
        """
        Отсортировать по цене, сначала дешевые
        """
        # найти выпадающий список сортировки
        self.sort_dropdown = self._driver.find_element(By.CLASS_NAME, 'chg-app-custom-dropdown__label')
        # нажать на выпадающий список сортировки
        self.sort_dropdown.click()
        # в выпавшем списке найти все методы способы сортировки
        self.sort_dropdown_list = self._driver.find_elements(By.CLASS_NAME, 'chg-app-dropdown-custom-item')
        # нажать на третий элемент в выпавшем списке
        self.sort_dropdown_list[2].click()

    def sort_expensive_first(self):
        """
        Отсортировать по цене, сначала дорогие
        """
        # найти выпадающий список сортировки
        self.sort_dropdown = self._driver.find_element(By.CLASS_NAME, 'chg-app-custom-dropdown__label')
        # нажать на выпадающий список сортировки
        self.sort_dropdown.click()
        # в выпавшем списке найти все методы способы сортировки
        self.sort_dropdown_list = self._driver.find_elements(By.CLASS_NAME, 'chg-app-dropdown-custom-item')
        # нажать на четвертый элемент в выпавшем списке
        self.sort_dropdown_list[3].click()


