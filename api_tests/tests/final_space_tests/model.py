from typing import List

from pydantic import BaseModel, HttpUrl


class Episode(BaseModel):
    id: int
    name: str
    air_date: str  # We'll parse it manually if needed, format: MM/DD/YYYY
    director: str
    writer: str
    characters: List[HttpUrl]
    img_url: HttpUrl
