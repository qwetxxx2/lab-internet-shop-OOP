from .base import BaseEntity


class CartItem(BaseEntity):
    TABLE = "cart_items"

    def __init__(self, entity_id, name, product_id, quantity):
        super().__init__(entity_id, name)
        self._product_id = product_id
        self._quantity = quantity

    # ===== ГЕТТЕРЫ / СЕТТЕРЫ =====
    @property
    def product_id(self):
        return self._product_id

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        if value <= 0:
            raise ValueError("Количество > 0")
        self._quantity = value

    # ===== БИЗНЕС-ЛОГИКА =====
    def add_quantity(self, amount: int):
        self._quantity += amount

    def remove_quantity(self, amount: int):
        if amount > self._quantity:
            raise ValueError("Слишком много")
        self._quantity -= amount

    def clear(self):
        """Очистить позицию"""
        self._quantity = 0

    def get_total_price(self, product: Product) -> float:
        """Стоимость позиции"""
        return product.price * self._quantity

    def get_info(self):
        return f"[CartItem] {self._name} | Product ID: {self._product_id} | Кол-во: {self._quantity}"

    def validate(self):
        return self._product_id > 0 and self._quantity > 0
