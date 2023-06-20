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

def get_game_id(cursor, game_name):
    """retrieves the given game's ID"""
    query = "SELECT id FROM games WHERE name=(?)"
    return cursor.execute(query, (game_name,)).fetchone()[0]

def insert_game(cursor, game_name):
    """ Inserts a game into the games table"""
    query = "INSERT INTO games (name) VALUES (?)"
    cursor.execute(query, (game_name,))

def basic_insert_query(cursor, table, game_name, var):
    """Used to insert data into tables"""
    match table:
        case "date":
            query = f"INSERT INTO {table} (date, game_id) VALUES (?,?)"
        case "desire":
            query = f"INSERT INTO {table} (desire, game_id) VALUES (?,?)"
        case _:
            query = f"INSERT INTO {table} ({table}_name, game_id) VALUES (?,?)"
    game_id = get_game_id(cursor, game_name)
    cursor.execute(query, (var, game_id))

def main():
    """ main method """
    conn = create_connection("./db/games.db")
    cursor = conn.cursor()
    sql_file = open("./queries/create_game_table.sql")
    query = sql_file.read()
    cursor.executescript(query)
    game_name = input("Which game would you like to add to your backlog?\n")
    insert_game(cursor, game_name)
    plat = input("For which Platform?\n")
    basic_insert_query(cursor, "platform", game_name, plat)

    for row in cursor.execute("SELECT * FROM games"):
        print(row)

    for row in cursor.execute("SELECT * FROM platform"):
        print(row)
    
if __name__ == "__main__":
    main()