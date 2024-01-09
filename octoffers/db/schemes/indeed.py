import sqlite3
from os import environ

db = sqlite3.connect(f"{environ['HOME']}/.config/octoffers/indeed.db")
with db:
    db.execute(
        """
        CREATE TABLE IF NOT EXISTS jobs (
            id INTEGER PRIMARY KEY,
            job_id TEXT,
            role TEXT,
            link TEXT,
            description TEXT,
            easy_apply BOOLEAN DEFAULT FALSE,
            cv_sent BOOLEAN DEFAULT FALSE,
            applicable BOOLEAN DEFAULT TRUE
        )
    """
    )
    db.commit()
