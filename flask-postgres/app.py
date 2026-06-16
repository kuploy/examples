import os
import psycopg
from flask import Flask

app = Flask(__name__)
DATABASE_URL = os.environ["DATABASE_URL"]  # injected by the stack connection


def init_db():
    with psycopg.connect(DATABASE_URL) as conn:
        conn.execute("CREATE TABLE IF NOT EXISTS visits (count int)")
        if conn.execute("SELECT count(*) FROM visits").fetchone()[0] == 0:
            conn.execute("INSERT INTO visits VALUES (0)")


@app.route("/")
def home():
    with psycopg.connect(DATABASE_URL) as conn:
        conn.execute("UPDATE visits SET count = count + 1")
        n = conn.execute("SELECT count FROM visits").fetchone()[0]
    return f"Hello from Kuploy Stacks! Visits: {n}"


init_db()
