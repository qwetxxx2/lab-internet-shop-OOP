from .base import BaseEntity


class Product(BaseEntity):
    TABLE = "products"

    def __init__(self, entity_id, name, price, stock):
        super().__init__(entity_id, name)
        self._price = price
        self._stock = stock

    # ===== ГЕТТЕРЫ / СЕТТЕРЫ =====
    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value <= 0:
            raise ValueError("Цена должна быть > 0")
        self._price = value

    @property
    def stock(self):
        return self._stock

    @stock.setter
    def stock(self, value):
        if value < 0:
            raise ValueError("Остаток не может быть отрицательным")
        self._stock = value

    # ===== БИЗНЕС-ЛОГИКА =====
    def decrease_stock(self, amount: int):
        if amount > self._stock:
            raise ValueError("Недостаточно товара")
        self._stock -= amount

    def increase_stock(self, amount: int):
        self._stock += amount

    def apply_discount(self, percent: float):
        """Скидка"""
        if percent < 0 or percent > 100:
            raise ValueError("Некорректная скидка")
        self._price *= (1 - percent / 100)

    def is_available(self) -> bool:
        """Есть ли товар в наличии"""
        return self._stock > 0

    # ===== ОБЯЗАТЕЛЬНЫЕ =====
    def get_info(self):
        return f"[Product] {self._name} | Цена: {self._price:.2f} | Остаток: {self._stock}"

    def validate(self):
        return self._price > 0 and self._stock >= 0