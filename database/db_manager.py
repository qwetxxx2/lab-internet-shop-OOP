import sqlite3
from models.product import Product
from models.cart_item import CartItem


class DatabaseManager:
    def __init__(self, db_name="shop.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    # =========================
    # CREATE TABLES
    # =========================
    def create_tables(self):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            price REAL,
            stock INTEGER
        )
        """)

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS cart_items (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            product_id INTEGER,
            quantity INTEGER
        )
        """)
        self.conn.commit()

    # =========================
    # ADD
    # =========================
    def add(self, obj):
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
                (obj.name, obj.product_id, obj.quantity)
            )

        self.conn.commit()

    # =========================
    # UPDATE
    # =========================
    def update(self, obj):
        if isinstance(obj, Product):
            self.cursor.execute(
                "UPDATE products SET name=?, price=?, stock=? WHERE id=?",
                (obj.name, obj.price, obj.stock, obj.id)
            )

        elif isinstance(obj, CartItem):
            self.cursor.execute(
                "UPDATE cart_items SET name=?, product_id=?, quantity=? WHERE id=?",
                (obj.name, obj.product_id, obj.quantity, obj.id)
            )

        self.conn.commit()

    # =========================
    # DELETE
    # =========================
    def delete(self, entity_id, cls):
        self.cursor.execute(f"DELETE FROM {cls.TABLE} WHERE id=?", (entity_id,))
        self.conn.commit()

    # =========================
    # GET BY ID
    # =========================
    def get_by_id(self, entity_id, cls):
        self.cursor.execute(f"SELECT * FROM {cls.TABLE} WHERE id=?", (entity_id,))
        row = self.cursor.fetchone()
        return self._map(row, cls) if row else None

    # =========================
    # GET ALL
    # =========================
    def get_all(self, cls):
        self.cursor.execute(f"SELECT * FROM {cls.TABLE}")
        return [self._map(r, cls) for r in self.cursor.fetchall()]

    # =========================
    # FIND
    # =========================
    def find_by_criteria(self, cls, **kwargs):
        query = f"SELECT * FROM {cls.TABLE} WHERE "
        query += " AND ".join([f"{k}=?" for k in kwargs])

        self.cursor.execute(query, tuple(kwargs.values()))
        return [self._map(r, cls) for r in self.cursor.fetchall()]
    def get_available_products(self):
        self.cursor.execute("SELECT * FROM products WHERE stock > 0")
        return [Product(*r) for r in self.cursor.fetchall()]

    def get_cart_total(self):
        """Общая сумма корзины"""
        self.cursor.execute("""
        SELECT SUM(p.price * c.quantity)
        FROM cart_items c
        JOIN products p ON c.product_id = p.id
        """)
        result = self.cursor.fetchone()[0]
        return result if result else 0

    # =========================
    # MAPPER
    # =========================
    def _map(self, row, cls):
        if cls == Product:
            return Product(*row)
        elif cls == CartItem:
            return CartItem(*row)