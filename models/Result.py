# models/Result.py

import sqlite3
from datetime import datetime

DB_PATH = "Game.db"  


class Result:
    """Handles saving and loading spelling test results."""

    def __init__(self, person_name, word, user_answer, accuracy):
        self.person_name = person_name
        self.word = word
        self.user_answer = user_answer
        self.accuracy = accuracy
        self.date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    @staticmethod
    def create_table():
        """Create results table if it doesn't exist."""
        conn = sqlite3.connect(DB_PATH)
        cur = conn.cursor()
        cur.execute(
            """
            CREATE TABLE IF NOT EXISTS results (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                person_name TEXT,
                word TEXT,
                user_answer TEXT,
                accuracy REAL,
                date TEXT
            )
            """
        )
        conn.commit()
        conn.close()

    def save(self):
        """Save the result to the database."""
        conn = sqlite3.connect(DB_PATH)
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO results (person_name, word, user_answer, accuracy, date) VALUES (?, ?, ?, ?, ?)",
            (self.person_name, self.word, self.user_answer, self.accuracy, self.date),
        )
        conn.commit()
        conn.close()

    @staticmethod
    def get_results_for_person(person_name):
        """Retrieve all results for a given user."""
        conn = sqlite3.connect(DB_PATH)
        cur = conn.cursor()
        cur.execute(
            "SELECT word, user_answer, accuracy, date FROM results WHERE person_name = ? ORDER BY date DESC",
            (person_name,),
        )
        results = cur.fetchall()
        conn.close()
        return results
