import sqlite3

def main():

    conn = sqlite3.connect('students.db')
    cursor = conn.cursor()

    # table

    cursor.executescript("""
        DROP TABLE IF EXISTS students;

        CREATE TABLE students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            full_name TEXT NOT NULL,
            city TEXT,
            country TEXT,
            birth_date TEXT,
            email TEXT,
            phone TEXT,
            group_name TEXT,
            average_grade REAL,
            subject TEXT,
            subject_avg_grade REAL
        );
    """)

    # table and infa
    cursor.executemany("""
        INSERT INTO students (
            full_name, city, country, birth_date,
            email, phone, group_name,
            average_grade, subject, subject_avg_grade
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, [
        ('Борис Коваленко', 'Київ', 'Україна', '2005-03-12',
         'boris@gmail.com', '0977771234', 'CS-21', 82.5, 'Математика', 78),

        ('Борис Коваленко', 'Київ', 'Україна', '2005-03-12',
         'boris@gmail.com', '0977771234', 'CS-21', 82.5, 'Фізика', 87),

        ('Марія Іваненко', 'Львів', 'Україна', '2004-06-25',
         'maria@gmail.com', '0991112233', 'CS-22', 90.2, 'Математика', 95),

        ('Марія Іваненко', 'Львів', 'Україна', '2004-06-25',
         'maria@gmail.com', '0991112233', 'CS-22', 90.2, 'Фізика', 85),

        ('Олег Петренко', 'Одеса', 'Україна', '2003-11-02',
         'oleg@gmail.com', '0507778899', 'CS-23', 74.0, 'Математика', 65),

        ('Олег Петренко', 'Одеса', 'Україна', '2003-11-02',
         'oleg@gmail.com', '0507778899', 'CS-23', 74.0, 'Фізика', 83)
    ])

    conn.commit()

    #1


    print("\nВся інформація:")
    cursor.execute("SELECT * FROM students")
    for row in cursor.fetchall():
        print(row)

    print("\n ПІБ студентів:")
    cursor.execute("SELECT DISTINCT full_name FROM students")
    for row in cursor.fetchall():
        print(row)

    print("\nСередні оцінки за рік:")
    cursor.execute("""
        SELECT DISTINCT full_name, average_grade
        FROM students
    """)
    for row in cursor.fetchall():
        print(row)

    print("\nСтуденти з мінімальною оцінкою > 70:")
    cursor.execute("""
        SELECT full_name
        FROM students
        GROUP BY full_name
        HAVING MIN(subject_avg_grade) > 70
    """)
    for row in cursor.fetchall():
        print(row)

    print("\nКраїни (унікальні):")
    cursor.execute("SELECT DISTINCT country FROM students")
    print(cursor.fetchall())

    print("\nМіста (унікальні):")
    cursor.execute("SELECT DISTINCT city FROM students")
    print(cursor.fetchall())

    print("\nГрупи (унікальні):")
    cursor.execute("SELECT DISTINCT group_name FROM students")
    print(cursor.fetchall())

    print("\nПредмет з мінімальною середньою оцінкою:")
    cursor.execute("""
        SELECT subject, subject_avg_grade
        FROM students
        WHERE subject_avg_grade = (
            SELECT MIN(subject_avg_grade) FROM students
        )
    """)
    print(cursor.fetchone())

    print("\nПредмет з максимальною середньою оцінкою:")
    cursor.execute("""
        SELECT subject, subject_avg_grade
        FROM students
        WHERE subject_avg_grade = (
            SELECT MAX(subject_avg_grade) FROM students
        )
    """)
    print(cursor.fetchone())

    #2

    print("\nМінімальна оцінка в діапазоні 60–80:")
    cursor.execute("""
        SELECT full_name
        FROM students
        GROUP BY full_name
        HAVING MIN(subject_avg_grade) BETWEEN 60 AND 80
    """)
    print(cursor.fetchall())

    print("\nСтуденти, яким 20 років:")
    cursor.execute("""
        SELECT *
        FROM students
        WHERE (strftime('%Y', 'now') - strftime('%Y', birth_date)) = 20
    """)
    print(cursor.fetchall())

    print("\nСтуденти віком 18–22:")
    cursor.execute("""
        SELECT *
        FROM students
        WHERE (strftime('%Y', 'now') - strftime('%Y', birth_date))
              BETWEEN 18 AND 22
    """)
    print(cursor.fetchall())

    print("\nСтуденти з імʼям Борис:")
    cursor.execute("""
        SELECT *
        FROM students
        WHERE full_name LIKE 'Борис%'
    """)
    print(cursor.fetchall())

    print("\nТелефон містить 777:")
    cursor.execute("""
        SELECT *
        FROM students
        WHERE phone LIKE '%777%'
    """)
    print(cursor.fetchall())

    print("\nEmail починається з 'm':")
    cursor.execute("""
        SELECT email
        FROM students
        WHERE email LIKE 'm%'
    """)
    print(cursor.fetchall())

    conn.close()


if __name__ == '__main__':
    main()
