# Интернет-магазин (товары/корзина) (Python + SQLite)

## 🧾 Задача

Закрепление принципов объектно-ориентированного программирования 
(инкапсуляция, наследование, полиморфизм, абстракция) 
на примере разработки модели предметной области 
«Интернет-магазин (товары/корзина)» с интеграцией с базой данных.

---

## 📌 Описание проекта

Проект представляет собой систему интернет-магазина, 
реализованную с использованием Python и SQLite.

Система поддерживает:

- хранение товаров
- управление корзиной
- валидацию данных
- работу с базой данных

---

## 🧱 Архитектура проекта

- Models → сущности (Product, CartItem)
- DatabaseManager → работа с БД
- SQLite → хранение данных

UML-диаграмма:
```mermaid
classDiagram

%% ======================
%% БАЗОВЫЙ КЛАСС
%% ======================
class BaseEntity {
    <<abstract>>
    - _id: int
    - _name: str

    + id: int
    + name: str

    + get_info() str
    + validate() bool
}

%% ======================
%% ТОВАР
%% ======================
class Product {
    - _price: float
    - _stock: int

    + price: float
    + stock: int

    + get_info() str
    + validate() bool

    + decrease_stock(amount: int) void
    + increase_stock(amount: int) void
}

%% ======================
%% КОРЗИНА
%% ======================
class CartItem {
    - _product_id: int
    - _quantity: int

    + product_id: int
    + quantity: int

    + get_info() str
    + validate() bool

    + add_quantity(amount: int) void
    + remove_quantity(amount: int) void
}

%% ======================
%% МЕНЕДЖЕР БД
%% ======================
class DatabaseManager {
    - conn
    - cursor

    + create_tables() void
    + save(obj: BaseEntity) void
    + get_all_products() List~Product~
    + get_all_cart_items() List~CartItem~
}

%% ======================
%% СВЯЗИ
%% ======================

BaseEntity <|-- Product
BaseEntity <|-- CartItem

DatabaseManager --> Product
DatabaseManager --> CartItem
