import sqlite3

def main():
    conn = sqlite3.connect(r'C:\Users\User\PycharmProjects\PythonProject1\SQL\hospital.sqlite')
    conn.execute('PRAGMA foreign_keys=ON;')
    cursor = conn.cursor()

    cursor.executescript("""
        -- Видалення старих таблиць
        DROP TABLE IF EXISTS Wards;
        DROP TABLE IF EXISTS Examinations;
        DROP TABLE IF EXISTS Doctors;
        DROP TABLE IF EXISTS Diseases;
        DROP TABLE IF EXISTS Departments;

        -- Departments
        CREATE TABLE Departments (
            Id INTEGER PRIMARY KEY AUTOINCREMENT,
            Building INTEGER NOT NULL CHECK(Building BETWEEN 1 AND 5),
            Financing NUMERIC NOT NULL DEFAULT 0 CHECK(Financing >= 0),
            Name TEXT NOT NULL UNIQUE CHECK(LENGTH(Name) > 0)
        );

        -- Diseases
        CREATE TABLE Diseases (
            Id INTEGER PRIMARY KEY AUTOINCREMENT,
            Name TEXT NOT NULL UNIQUE CHECK(LENGTH(Name) > 0),
            Severity INTEGER NOT NULL DEFAULT 1 CHECK(Severity >= 1)
        );

        -- Doctors
        CREATE TABLE Doctors (
            Id INTEGER PRIMARY KEY AUTOINCREMENT,
            Name TEXT NOT NULL CHECK(LENGTH(Name) > 0),
            Surname TEXT NOT NULL CHECK(LENGTH(Surname) > 0),
            Phone CHAR(10),
            Salary NUMERIC NOT NULL CHECK(Salary > 0)
        );

        -- Examinations
        CREATE TABLE Examinations (
            Id INTEGER PRIMARY KEY AUTOINCREMENT,
            Name TEXT NOT NULL UNIQUE CHECK(LENGTH(Name) > 0),
            DayOfWeek INTEGER NOT NULL CHECK(DayOfWeek BETWEEN 1 AND 7),
            StartTime TEXT NOT NULL CHECK(StartTime BETWEEN '08:00' AND '18:00'),
            EndTime TEXT NOT NULL CHECK(EndTime > StartTime)
        );

        -- Wards
        CREATE TABLE Wards (
            Id INTEGER PRIMARY KEY AUTOINCREMENT,
            Name TEXT NOT NULL UNIQUE CHECK(LENGTH(Name) > 0),
            Building INTEGER NOT NULL CHECK(Building BETWEEN 1 AND 5),
            Floor INTEGER NOT NULL CHECK(Floor >= 1)
        );
    """)


    cursor.executemany(
        "INSERT INTO Departments (Building, Financing, Name) VALUES (?, ?, ?)",
        [
            (1, 50000, 'Cardiology'),
            (2, 30000, 'Neurology'),
            (3, 40000, 'Pediatrics')
        ]
    )


    cursor.executemany(
        "INSERT INTO Diseases (Name, Severity) VALUES (?, ?)",
        [
            ('Flu', 2),
            ('COVID-19', 5),
            ('Migraine', 1)
        ]
    )

    cursor.executemany(
        "INSERT INTO Doctors (Name, Surname, Phone, Salary) VALUES (?, ?, ?, ?)",
        [
            ('Ivan', 'Ivanov', '0991234567', 1000),
            ('Maria', 'Petrova', '0679876543', 1200)
        ]
    )

    cursor.executemany(
        "INSERT INTO Examinations (Name, DayOfWeek, StartTime, EndTime) VALUES (?, ?, ?, ?)",
        [
            ('Blood Test', 1, '09:00', '10:00'),
            ('X-Ray', 2, '10:30', '11:30')
        ]
    )


    cursor.executemany(
        "INSERT INTO Wards (Name, Building, Floor) VALUES (?, ?, ?)",
        [
            ('Ward A', 1, 1),
            ('Ward B', 2, 3)
        ]
    )

    conn.commit()

    cursor.execute("SELECT * FROM Departments")
    print("Departments:", cursor.fetchall())

    cursor.execute("SELECT * FROM Diseases")
    print("Diseases:", cursor.fetchall())

    cursor.execute("SELECT * FROM Doctors")
    print("Doctors:", cursor.fetchall())

    cursor.execute("SELECT * FROM Examinations")
    print("Examinations:", cursor.fetchall())

    cursor.execute("SELECT * FROM Wards")
    print("Wards:", cursor.fetchall())

    conn.close()

if __name__ == "__main__":
    main()


