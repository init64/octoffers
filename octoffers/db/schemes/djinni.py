import sqlite3
from os import environ

db = sqlite3.connect(f"{environ['HOME']}/.config/octoffers/djinni.db")
with db:
    db.execute(
        """
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
    """
    )
    db.commit()
