from .base import BaseEntity


class CartItem(BaseEntity):
    TABLE = "cart_items"

    def __init__(self, entity_id, name, product_id, quantity):
        super().__init__(entity_id, name)
        self._product_id = product_id
        self._quantity = quantity

    def get_info(self):
        return f"{self._name} | Product ID: {self._product_id} | Кол-во: {self._quantity}"

    def validate(self):
        return self._product_id > 0 and self._quantity > 0