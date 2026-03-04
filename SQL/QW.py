import sqlite3
import random

def main():
    conn = sqlite3.connect('db.sqlite')
    conn.execute('PRAGMA foreign_keys=ON;')
    cursor = conn.cursor()

    # Створення таблиць
    cursor.executescript("""
        DROP TABLE IF EXISTS orders;
        DROP TABLE IF EXISTS products;

        CREATE TABLE products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL UNIQUE,
            price NUMERIC NOT NULL CHECK (price >= 0),
            stock INTEGER NOT NULL CHECK (stock >= 0)
        );

        CREATE TABLE orders (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            product_id INTEGER NOT NULL,
            quantity INTEGER NOT NULL CHECK (quantity > 0),
            total_price NUMERIC NOT NULL,
            order_date DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
            customer_name TEXT DEFAULT 'Anonymous',
            FOREIGN KEY (product_id) REFERENCES products(id) ON DELETE CASCADE
        );
    """)

    # Додавання продуктів
    cursor.executemany(
        "INSERT INTO products (name, price, stock) VALUES (?, ?, ?)",
        [
            ('iphone 15', 600, 10),
            ('iphone 16', 700, 10),
            ('iphone 7', 800, 10),
            ('samsung galaxy 23', 900, 10)
        ]
    )

    # Додавання кількох замовлень з випадковими кількостями та клієнтами
    customers = ['Katerina', 'Oleh', 'Anna', 'Max']
    for _ in range(10):  # 10 замовлень
        model_id = random.randint(1, 4)
        cursor.execute("SELECT price, stock FROM products WHERE id = ?", (model_id,))
        product_price, stock = cursor.fetchone()

        if stock == 0:
            continue  # пропускаємо, якщо товару немає

        quantity = random.randint(1, stock)
        total_price = product_price * quantity
        customer = random.choice(customers)

        cursor.execute(
            "INSERT INTO orders (product_id, quantity, total_price, customer_name) VALUES (?, ?, ?, ?)",
            (model_id, quantity, total_price, customer)
        )

        cursor.execute(
            "UPDATE products SET stock = stock - ? WHERE id = ?",
            (quantity, model_id)
        )

    conn.commit()

    # Вивід продуктів
    print("Products:")
    cursor.execute("SELECT * FROM products")
    for row in cursor.fetchall():
        print(row)

    # Вивід замовлень
    print("\nOrders:")
    cursor.execute("""
        SELECT products.name, products.price, orders.quantity, orders.total_price, orders.customer_name, orders.order_date
        FROM orders
        JOIN products ON orders.product_id = products.id;
    """)
    for row in cursor.fetchall():
        print(row)

    # 1) Кількість замовлень по товарам
    print("\n1) Total orders per product:")
    cursor.execute("""
        SELECT products.name, COUNT(*) AS total_orders
        FROM orders
        JOIN products ON orders.product_id = products.id
        GROUP BY products.id
    """)
    for row in cursor.fetchall():
        print(row)

    # 2) Середня сума замовлення по товарам
    print("\n2) Average order total per product:")
    cursor.execute("""
        SELECT products.name, AVG(orders.total_price) AS avg_order
        FROM orders
        JOIN products ON orders.product_id = products.id
        GROUP BY products.id
    """)
    for row in cursor.fetchall():
        print(row)

    # 3) Загальна сума продажів по кожному дню
    print("\n3) Total sales per day:")
    cursor.execute("""
        SELECT DATE(order_date) AS order_day, SUM(total_price) AS total_sales
        FROM orders
        GROUP BY DATE(order_date)
        ORDER BY order_day
    """)
    for row in cursor.fetchall():
        print(row)

    # 4) Топ 3 товарів з найбільшою сумою продажів
    print("\n4) Top 3 products by total sales:")
    cursor.execute("""
        SELECT products.name, SUM(orders.total_price) AS total_sales
        FROM orders
        JOIN products ON orders.product_id = products.id
        GROUP BY products.id
        ORDER BY total_sales DESC
        LIMIT 3
    """)
    for row in cursor.fetchall():
        print(row)

    conn.close()


if __name__ == '__main__':
    main()
