from typing import List
from pydantic import BaseModel
from content_scraper.db.strings import WrittenContentCategory
from datetime import datetime


class TextContent(BaseModel):
    content: str
    author_username: str
    conversation_native_id: str
    publication_date: datetime
    publically_available: bool
    keywords: List[str]
    miscellanous: str


class ScrapeResult(BaseModel):
    platform: str
    contents: List[TextContent]
    content_type: WrittenContentCategory
