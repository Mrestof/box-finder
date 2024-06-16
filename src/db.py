from contextlib import contextmanager
from typing import Any, Generator
from sqlite3 import Cursor, connect
from pathlib import Path


DB_PATH = Path('segments.db')


@contextmanager
def get_cursor() -> Generator[Cursor, Any, None]:
    con = connect(DB_PATH)
    cur = con.cursor()
    try:
        yield cur
    finally:
        cur.close()
        con.close()
