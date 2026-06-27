from src.database.database import Database

class ScoreRepository:

    def save(self, player, points):

        conn = Database.connect()

        cursor = conn.cursor()

        cursor.execute(

            """
            INSERT INTO score(player, points)
            VALUES(?, ?)
            """,

            (player, points,)
        )

        conn.commit()

        conn.close()

    def best_score(self):
        conn = Database.connect()

        cursor = conn.cursor()

        cursor.execute("""

            SELECT MAX(points)

            FROM score

        """)

        best = cursor.fetchone()[0]

        conn.close()

        return best if best else 0

    def top5(self):
        conn = Database.connect()

        cursor = conn.cursor()

        cursor.execute("""

            SELECT player, points

            FROM score

            ORDER BY points DESC

            LIMIT 5

        """)

        rows = cursor.fetchall()

        conn.close()

        return rows

    def last_scores(self):
        conn = Database.connect()

        cursor = conn.cursor()

        cursor.execute("""

            SELECT points, created_at

            FROM score

            ORDER BY id DESC

            LIMIT 5

        """)

        rows = cursor.fetchall()

        conn.close()

        return rows
