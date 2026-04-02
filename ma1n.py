from database.db_manager import DatabaseManager
from models.product import Product
from models.cart_item import CartItem


def main():
    db = DatabaseManager()
    db.create_tables()

    p1 = Product(None, "Ноутбук", 1200, 5)
    p2 = Product(None, "Мышь", 25, 100)

    db.save(p1)
    db.save(p2)

    print("=== Товары ===")
    for p in db.get_all_products():
        print(p.get_info())

    cart = CartItem(None, "Корзина", 1, 2)
    db.save(cart)


if __name__ == "__main__":
    main()