from typing import List, Optional
from pydantic import BaseModel
from content_scraper.db.strings import WrittenContentCategory
from datetime import datetime


class AppMetadata(BaseModel):
    name: str
    publisher: str
    esrb_rating: str
    publication_date: datetime
    bundle_id: str


class TextContent(BaseModel):
    native_id: Optional[str] = None
    content: str
    author_username: str
    conversation_native_id: str
    publication_date: datetime
    publically_available: bool
    keywords: List[str]
    miscellanous: str


class ScrapeResult(BaseModel):
    source_platform: str
    contents: List[TextContent]
    content_type: WrittenContentCategory
    app_target: Optional[str] = None
