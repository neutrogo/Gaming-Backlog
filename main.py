import sqlite3
from sqlite3 import Error
import pandas as pd

def create_connection(path):
    """ Creates a connection to the Database defined by path, if none exists,
        a new Database is created
    """
    connection = None
    try:
        connection = sqlite3.connect(path)
        print("Successfully connected to the SQLite Database")
    except Error as e:
        print(f"Error: {e}")
    
    return connection

def main():
    """ main method """
    conn = create_connection("./db/games.db")

    cursor = conn.cursor()

    sql_file = open("./queries/create_game_table.sql")
    query = sql_file.read()
    cursor.executescript(query)
    cursor.execute("INSERT INTO games (name) VALUES ('Elden Ring')")

    for row in cursor.execute("SELECT * FROM games"):
        print(row)

if __name__ == "__main__":
    main()