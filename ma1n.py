from database.db_manager import DatabaseManager
from models.product import Product
from models.cart_item import CartItem


def main():
    db = DatabaseManager()
    db.create_tables()

    try:
        # =========================
        # СОЗДАНИЕ ТОВАРОВ
        # =========================
        p1 = Product(None, "Ноутбук", 1200, 5)
        p2 = Product(None, "Мышь", 25, 100)
        p3 = Product(None, "Монитор", 300, 0)

        db.add(p1)
        db.add(p2)
        db.add(p3)

        print("\n=== ВСЕ ТОВАРЫ ===")
        for p in db.get_all(Product):
            print(p.get_info())

        # =========================
        # БИЗНЕС-ЛОГИКА PRODUCT
        # =========================
        print("\n=== СКИДКА НА НОУТБУК ===")
        p1.apply_discount(10)
        db.update(p1)
        print(p1.get_info())

        print("\n=== ПРОВЕРКА НАЛИЧИЯ ===")
        print("Ноутбук доступен:", p1.is_available())
        print("Монитор доступен:", p3.is_available())

        print("\n=== УМЕНЬШЕНИЕ ОСТАТКА ===")
        p1.decrease_stock(2)
        db.update(p1)
        print(p1.get_info())

        # =========================
        # ДОСТУПНЫЕ ТОВАРЫ
        # =========================
        print("\n=== ТОВАРЫ В НАЛИЧИИ ===")
        for p in db.get_available_products():
            print(p.get_info())

        # =========================
        # КОРЗИНА
        # =========================
        print("\n=== ДОБАВЛЕНИЕ В КОРЗИНУ ===")

        cart1 = CartItem(None, "Корзина", 1, 2)
        cart2 = CartItem(None, "Корзина", 2, 3)

        db.add(cart1)
        db.add(cart2)

        for c in db.get_all(CartItem):
            print(c.get_info())

        # =========================
        # БИЗНЕС-ЛОГИКА CART
        # =========================
        print("\n=== ИЗМЕНЕНИЕ КОЛИЧЕСТВА ===")
        cart1.add_quantity(1)
        db.update(cart1)
        print(cart1.get_info())

        print("\n=== СТОИМОСТЬ ПОЗИЦИИ ===")
        product = db.get_by_id(cart1.product_id, Product)
        print("Сумма:", cart1.get_total_price(product))

        # =========================
        # ОБЩАЯ СУММА КОРЗИНЫ
        # =========================
        print("\n=== СУММА КОРЗИНЫ ===")
        print("Итого:", db.get_cart_total())

        # =========================
        # ПОИСК
        # =========================
        print("\n=== ПОИСК ТОВАРА ===")
        found = db.find_by_criteria(Product, name="Мышь")
        for f in found:
            print(f.get_info())

        # =========================
        # DELETE
        # =========================
        print("\n=== УДАЛЕНИЕ ===")
        db.delete(3, Product)

        print("После удаления:")
        for p in db.get_all(Product):
            print(p.get_info())

        # =========================
        # ОШИБКА (для отчета)
        # =========================
        print("\n=== ПРОВЕРКА ОШИБКИ ===")
        bad = Product(None, "Ошибка", -100, -5)
        db.add(bad)

    except Exception as e:
        print("\nОшибка:", e)


if __name__ == "__main__":
    main()