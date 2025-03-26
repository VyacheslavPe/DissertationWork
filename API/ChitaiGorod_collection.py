import requests
from specific_data import cart, product

class CG_API:
    def __init__(self, url : str, token : str):
        self.url = url
        self.token = token

    def add_to_cart(self, product_json : dict):
        """
        Запрос на добавление товара в корзину
        """
        return requests.post(self.url + cart + product, json=product_json, headers={'Authorization' : self.token})

    def remove_from_cart(self, product_id : str):
        """
        Запрос на удаление товара из корзины
        """
        return requests.delete(self.url + cart + product + product_id, headers={'Authorization' : self.token})

    def change_quantity_cart(self, quantity_json : dict):
        """
        Запрос на изменение количества товара в корзине
        """
        return requests.put(self.url + cart, json=quantity_json, headers={'Authorization' : self.token})

    def get_cart(self):
        """
        запрос на получение информации о корзине
        """
        return requests.get(self.url + cart, headers={'Authorization' : self.token})
