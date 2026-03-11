import sqlite3


def get_connection():

    conn = sqlite3.connect("data/database.db")
    return conn


def create_tables():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS user_progress (
        id INTEGER PRIMARY KEY,
        points INTEGER,
        level TEXT,
        questions_asked INTEGER,
        quizzes_taken INTEGER
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS quiz_history (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        topic TEXT,
        score INTEGER,
        total_questions INTEGER
    )
    """)

    conn.commit()
    conn.close()


def save_progress(points, level, questions_asked, quizzes_taken):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM user_progress")

    cursor.execute(
        """
        INSERT INTO user_progress
        (points, level, questions_asked, quizzes_taken)
        VALUES (?, ?, ?, ?)
        """,
        (points, level, questions_asked, quizzes_taken)
    )

    conn.commit()
    conn.close()


def load_progress():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM user_progress")

    row = cursor.fetchone()

    conn.close()

    return row


def save_quiz(topic, score, total):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO quiz_history
        (topic, score, total_questions)
        VALUES (?, ?, ?)
        """,
        (topic, score, total)
    )

    conn.commit()
    conn.close()