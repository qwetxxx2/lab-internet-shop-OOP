from .base import BaseEntity


class Product(BaseEntity):
    TABLE = "products"

    def __init__(self, entity_id, name, price, stock):
        super().__init__(entity_id, name)
        self._price = price
        self._stock = stock

    @property
    def price(self):
        return self._price

    @property
    def stock(self):
        return self._stock

    def get_info(self):
        return f"{self._name} | Цена: {self._price} | Остаток: {self._stock}"

    def validate(self):
        return self._price > 0 and self._stock >= 0