from contextlib import asynccontextmanager
from fastapi import FastAPI

from src.db import get_cursor


@asynccontextmanager
async def lifespan(app: FastAPI):
    # NOTE: db creation and updates to it should be managed via Alembic, but as
    # this is just a test task, I'm gonna omit migrations
    with get_cursor() as cur:
        # create the fast table with R-tree
        cur.execute("""
            CREATE VIRTUAL TABLE IF NOT EXISTS fast_segments USING rtree(
                id ROWID,    -- Integer primary key
                x1, x2,      -- Segment start and end on X axis
                y1, y2       -- Segment start and end on Y axis
            )
        """)
        # create the slow table so that we can compare the performance
        cur.execute("""
            CREATE TABLE IF NOT EXISTS slow_segments (
                id ROWID,    -- Integer primary key
                x1, x2,      -- Segment start and end on X axis
                y1, y2       -- Segment start and end on Y axis
            )
        """)
    yield
