from pydantic import BaseModel


class Segment(BaseModel):
    x1: float
    y1: float
    x2: float
    y2: float


class SegmentsResponse(BaseModel):
    segments: list[Segment]
