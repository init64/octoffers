import sqlite3


class DatabaseManager:
    def __init__(self, db_path):
        self.db = sqlite3.connect(db_path)
        self.create_tables()

    def create_tables(self):
        self.db.execute("""
            CREATE TABLE IF NOT EXISTS jobs (
                id INTEGER PRIMARY KEY,
                job_id TEXT,
                role TEXT,
                link TEXT,
                category TEXT,
                source TEXT,
                description TEXT,
                salary INT,
                matches BOOLEAN DEFAULT FALSE,
                cv_sent BOOLEAN DEFAULT FALSE
            )
        """)
        self.db.commit()