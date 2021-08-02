import sqlite3
from sqlite3 import Connection, Cursor


class RepositoryDecorator():
    def get_cursor(func):
        def wrap(*args, **kwargs):
            cursor : Cursor = args[0].connection.cursor()
            result = func(*args, **kwargs, cursor = cursor)
            return result
        return wrap


class ScoreRepository():
    connection : sqlite3.Connection

    def __init__(self, path_to_db = "game.db"):
        self.connection = sqlite3.connect(path_to_db)
        self.initialize_score_db()
    
    @RepositoryDecorator.get_cursor
    def initialize_score_db(self, cursor: Cursor):
        query = """create table if not exists game_values (key text primary key, value blob);"""
        cursor.execute(query)

        query = """insert INTO game_values(key, value) SELECT 'score', 0 where not EXISTS (select 1 from game_values where key = 'score') """
        cursor.execute(query)


    @RepositoryDecorator.get_cursor
    def get_score(self, cursor: Cursor) -> int:
        
        cursor.execute("""select * from game_values where key = 'score'""")
        data = cursor.fetchall()
        key, value = data[0]
        return int(value)

    @RepositoryDecorator.get_cursor
    def update_score(self, score: int, cursor: Cursor):
        
        score = int(score)

        query = """update game_values set value = ? where key = 'score'"""
        params = (score,)
        cursor.execute(query, params)



