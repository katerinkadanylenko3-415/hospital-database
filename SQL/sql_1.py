import sqlite3
import random

def main():
    conn = sqlite3.connect('db4.sqlite')
    conn.execute('PRAGMA foreign_keys=ON;')
    cursor = conn.cursor()

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
            FOREIGN KEY (product_id) REFERENCES products(id) ON DELETE CASCADE
        );
        
    """)

    cursor.executemany(
        "INSERT INTO products (name, price, stock) VALUES (?, ?, ?)",
        [
            ('iphone 15', 600, 10),
            ('iphone 16', 700, 10),
            ('iphone 7', 800, 10),
            ('samsung galaxy 23', 900, 10)
        ]
    )


    model_id = random.randint(1, 4)
    cursor.execute("SELECT price, stock FROM products WHERE id = ?", (model_id,))
    product_price, stock = cursor.fetchone()

    quantity = random.randint(1, stock)
    total_price = product_price * quantity


    cursor.execute(
        "INSERT INTO orders (product_id, quantity, total_price) VALUES (?, ?, ?)",
        (model_id, quantity, total_price)
    )

    cursor.execute(
        "UPDATE products SET stock = stock - ? WHERE id = ?",
        (quantity, model_id)
    )

    conn.commit()



    cursor.execute("SELECT * FROM products")
    print("Products:")

    # cursor.execute("SELECT * FROM products WHERE name LIKE 'iphone 1_'")
    # cursor.execute("SELECT * FROM products WHERE name LIKE 'sam%'")
    # cursor.execute("UPDATE products SET stock = ? WHERE id = ?", (9, 2))
    # cursor.execute("SELECT * FROM products;")

    cursor.execute("""
        SELECT products.name, products.price, orders.quantity, orders.total_price
        FROM orders
        JOIN products ON orders.product_id = products.id;
    """)


    #count() - підрахунок кількості

    cursor.execute("SELECT COUNT(*) AS total_orders FROM orders")

    cursor.execute("SELECT COUNT(DISTINCT product_id) FROM orders")

    #SUM()
    cursor.execute("SELECT SUM(total_price) FROM orders")
    cursor.execute("SELECT SUM(quantity) FROM orders")

    #AVG()

    cursor.execute("SELECT AVG(total_price) FROM orders")

    #MAX() - MIN()
    cursor.execute("SELECT MAX(total_price) FROM orders")

    # cursor.execute("""SELECT product_id, SUM(total-price) AS total_sales
    #                   FROM orders
    #                   GROUP BY product_id
    #                   """)

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


    cursor.execute("""CREATE TABLE IF NOT EXISTS users(
       id INTEGER PRIMARY KEY AUTOINCREMENT,
       name TEXT NOT NULL,
       email TEXT UNIQUE NOT NULL
      )  ;
      
      ALTER TABLE orders ADD COLUMN user_id
      INTEGER REFERENCES users(id) ON DELETE CASCADE;
      
      INSERT INTO users (name, email) VALUES (?, ?)
      ('Lion', 'lion@gmail.com'),
      ('Maria', 'maria@gmail.com'),
      ('Borus', 'borus@gmail.com');
      
    """)


    for row in cursor.fetchall():
        print(row)


    conn.commit()

    # cursor.execute("SELECT * FROM products ORDER BY price DESC LIMIT 1;")
    # print("Top-1 most expensive product:")
    # print(cursor.fetchone())
    #
    # cursor.execute("SELECT * FROM orders ORDER BY quantity DESC LIMIT 1;")
    # print("Biggest order by quantity:")
    # print(cursor.fetchone())


if __name__ == '__main__':
    main()


