from src.database.database import Database


def init_database():

    conn = Database.connect()

    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS score (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            points INTEGER NOT NULL,

            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

        );
    """)

    conn.commit()

    conn.close()