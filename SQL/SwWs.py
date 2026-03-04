import sqlite3
import random


def main():
    conn = sqlite3.connect('sales.sqlite')
    conn.execute("PRAGMA foreign_keys = ON;")
    cursor = conn.cursor()


    cursor.executescript("""
        DROP TABLE IF EXISTS Sales;
        DROP TABLE IF EXISTS Salesmen;
        DROP TABLE IF EXISTS Customers;




        CREATE TABLE Salesmen (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            city TEXT
        );



        CREATE TABLE Customers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            city TEXT
        );



        CREATE TABLE Sales (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            amount REAL NOT NULL CHECK(amount >= 0),
            sale_date DATETIME DEFAULT CURRENT_TIMESTAMP,
            salesman_id INTEGER,
            customer_id INTEGER,
            FOREIGN KEY (salesman_id) REFERENCES Salesmen(id),
            FOREIGN KEY (customer_id) REFERENCES Customers(id)
        );
    """)


    salesmen_data = [
        ("John", "London"),
        ("Maria", "Paris"),
        ("Alex", "Berlin")
    ]


    customers_data = [
        ("Olga", "Kyiv"),
        ("Ivan", "Lviv"),
        ("Anna", "Warsaw")
    ]

    cursor.executemany(
        "INSERT INTO Salesmen (name, city) VALUES (?, ?)",
        salesmen_data
    )

    cursor.executemany(
        "INSERT INTO Customers (name, city) VALUES (?, ?)",
        customers_data
    )

    for _ in range(10):
        amount = random.randint(100, 1000)
        salesman_id = random.randint(1, 3)
        customer_id = random.randint(1, 3)

        cursor.execute("""
            INSERT INTO Sales (amount, salesman_id, customer_id)
            VALUES (?, ?, ?)
        """, (amount, salesman_id, customer_id))



    conn.commit()


    print("\n1) Усі угоди:")
    cursor.execute("SELECT * FROM Sales")
    for row in cursor.fetchall():
        print(row)

    print("\n2) Угоди конкретного продавця:")
    cursor.execute("SELECT * FROM Sales WHERE salesman_id = 1")
    print(cursor.fetchall())




    print("\n3) Максимальна угода:")
    cursor.execute("""
        SELECT * FROM Sales
        WHERE amount = (SELECT MAX(amount) FROM Sales)
    """)
    print(cursor.fetchall())


    print("\n4) Мінімальна угода:")
    cursor.execute("""
        SELECT * FROM Sales
        WHERE amount = (SELECT MIN(amount) FROM Sales)
    """)
    print(cursor.fetchall())


    print("\n5) Максимальна угода продавця (id=1):")
    cursor.execute("""
        SELECT * FROM Sales
        WHERE salesman_id = 1
        AND amount = (
            SELECT MAX(amount)
            FROM Sales
            WHERE salesman_id = 1
        )
    """)
    print(cursor.fetchall())



    print("\n6) Мінімальна угода продавця (id=1):")
    cursor.execute("""
        SELECT * FROM Sales
        WHERE salesman_id = 1
        AND amount = (
            SELECT MIN(amount)
            FROM Sales
            WHERE salesman_id = 1
        )
    """)
    print(cursor.fetchall())


    print("\n7) Максимальна угода покупця (id=1):")
    cursor.execute("""
        SELECT * FROM Sales
        WHERE customer_id = 1
        AND amount = (
            SELECT MAX(amount)
            FROM Sales
            WHERE customer_id = 1
        )
    """)
    print(cursor.fetchall())




    print("\n8) Мінімальна угода покупця (id=1):")
    cursor.execute("""
        SELECT * FROM Sales
        WHERE customer_id = 1
        AND amount = (
            SELECT MIN(amount)
            FROM Sales
            WHERE customer_id = 1
        )
    """)
    print(cursor.fetchall())


    print("\n9) Продавець з максимальною сумою продажів:")
    cursor.execute("""
        SELECT Salesmen.name, SUM(Sales.amount) AS total_sales
        FROM Sales
        JOIN Salesmen ON Sales.salesman_id = Salesmen.id
        GROUP BY Salesmen.id
        ORDER BY total_sales DESC
        LIMIT 1
    """)
    print(cursor.fetchall())




    print("\n10) Продавець з мінімальною сумою продажів:")
    cursor.execute("""
        SELECT Salesmen.name, SUM(Sales.amount) AS total_sales
        FROM Sales
        JOIN Salesmen ON Sales.salesman_id = Salesmen.id
        GROUP BY Salesmen.id
        ORDER BY total_sales ASC
        LIMIT 1
    """)
    print(cursor.fetchall())



    print("\n11) Покупець з максимальною сумою покупок:")
    cursor.execute("""
        SELECT Customers.name, SUM(Sales.amount) AS total_purchases
        FROM Sales
        JOIN Customers ON Sales.customer_id = Customers.id
        GROUP BY Customers.id
        ORDER BY total_purchases DESC
        LIMIT 1
    """)
    print(cursor.fetchall())


    print("\n12) Середня сума покупок покупця (id=1):")
    cursor.execute("""
        SELECT AVG(amount)
        FROM Sales
        WHERE customer_id = 1
    """)
    print(cursor.fetchall())


    print("\n13) Середня сума продажів продавця (id=1):")
    cursor.execute("""
        SELECT AVG(amount)
        FROM Sales
        WHERE salesman_id = 1
    """)
    print(cursor.fetchall())

    conn.close()


if __name__ == "__main__":
    main()
