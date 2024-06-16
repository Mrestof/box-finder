from sqlite3 import Cursor
from typing import Annotated
from fastapi import Depends, FastAPI

from src.schemas import Segment, SegmentsResponse
from src.lifespan import lifespan
from src.db import get_cursor


app = FastAPI(
    lifespan=lifespan,
    version='1.0.0',
    title='Segment storage',
    description='Test task for segment querying.',
)


@app.get(
    '/segments',
    description='Get segments intersecting with the input segment.'
)
def segments(segment: Annotated[Segment, Depends()]) -> SegmentsResponse:
    with get_cursor() as cur:
        print(cur)
        result = cur.execute("""
            select x1, y1, x2, y2 from fast_segments
                where :x1 < x2
                and :x2 > x1
                and :y1 < y2
                and :y2 > y1
        """, dict(segment))
        print(result.fetchall())
    return SegmentsResponse(segments=[])


@app.post(
    '/segments',
    description='Fill the segments table with pseudo random data'
)
def fill_segments() -> None:
    ...
