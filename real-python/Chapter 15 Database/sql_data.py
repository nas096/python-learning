import sqlite3
from pathlib import Path

values = (
    ("Jean-Baptiste Zorg", "Human", 122),
    ("Korben Dallas", "Meat Popsicle", 100),
    ("Ak'not", "Mangalore", -5)
)

with sqlite3.connect("test_database.db") as connection:
    cursor = connection.cursor()
    cursor.execute(
        """
        CREATE TABLE Roster(
            Name TEXT,
            Species TEXT,
            IQ INT
        );
       """ 
    )

    cursor.executemany("INSERT INTO Roster VALUES(?,?,?)", values)

    cursor.execute(
        "UPDATE Roster SET Species=? WHERE Name=? AND IQ=?;",
        ("Human", "Korben Dallas", 100)
    )

    cursor.execute("SELECT Name, IQ from Roster WHERE Species='Human';"
    )

    for row in cursor.fetchall():
        print(row)