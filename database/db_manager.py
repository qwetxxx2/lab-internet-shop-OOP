import sqlite3
from models.product import Product
from models.cart_item import CartItem


class DatabaseManager:
    def __init__(self, db_name="shop.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    def create_tables(self):
        with open("database/schema.sql", "r", encoding="utf-8") as f:
            self.cursor.executescript(f.read())
        self.conn.commit()

    def save(self, obj):
        if not obj.validate():
            raise ValueError("Ошибка валидации")

        if isinstance(obj, Product):
            self.cursor.execute(
                "INSERT INTO products (name, price, stock) VALUES (?, ?, ?)",
                (obj.name, obj.price, obj.stock)
            )

        elif isinstance(obj, CartItem):
            self.cursor.execute(
                "INSERT INTO cart_items (name, product_id, quantity) VALUES (?, ?, ?)",
                (obj.name, obj._product_id, obj._quantity)
            )

        self.conn.commit()

    def get_all_products(self):
        self.cursor.execute("SELECT * FROM products")
        return [Product(*row) for row in self.cursor.fetchall()]