import sqlite3
from sqlite3 import Connection, Cursor


class RepositoryDecorator:
    def get_cursor_and_commit(func):
        """Initializes a cursor, commits at the end of the function."""

        def wrap(*args, **kwargs):
            connection: Connection = args[0].connection
            cursor: Cursor = connection.cursor()
            result = func(*args, **kwargs, cursor=cursor)
            args[0].connection.commit()
            return result

        return wrap


class ScoreRepository:
    connection: sqlite3.Connection

    def __init__(self, path_to_db="game.db"):
        self.connection = sqlite3.connect(path_to_db)
        self.initialize_score_db()

    @RepositoryDecorator.get_cursor_and_commit
    def initialize_score_db(self, cursor: Cursor):
        query = """create table if not exists game_values (key text primary key, value blob);"""
        cursor.execute(query)

        query = """insert INTO game_values(key, value) SELECT 'score', -1 where not EXISTS (select 1 from game_values where key = 'score') """
        cursor.execute(query)

    @RepositoryDecorator.get_cursor_and_commit
    def get_score(self, cursor: Cursor) -> int:

        cursor.execute("""select * from game_values where key = 'score'""")
        data = cursor.fetchall()

        if not data:
            return 0

        score_key, score_value = data[0]
        return int(score_value)

    @RepositoryDecorator.get_cursor_and_commit
    def update_score(self, score: int, cursor: Cursor):

        score = int(score)

        query = """update game_values set value = ? where key = 'score'"""
        params = (score,)
        cursor.execute(query, params)
