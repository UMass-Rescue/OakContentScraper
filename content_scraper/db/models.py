"""
Content Scraper models
"""
from sqlalchemy import Column, ForeignKey, String, UniqueConstraint, Enum
from sqlalchemy.types import DateTime, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func
from content_scraper.db.util import WrittenContentCategory


Base = declarative_base()


class TimestampMixin(object):
    created_at = Column(DateTime, default=func.now())


class Platforms(TimestampMixin, Base):
    """
    Source platforms
    """

    __tablename__ = "platforms"

    id = Column(String, primary_key=True)
    name = Column(String)


class TextContent(TimestampMixin, Base):
    """
    Written Text Content
    """

    __tablename__ = "text_contents"

    id = Column(String, primary_key=True)
    content = Column(String)
    __table_args__ = (UniqueConstraint("id", sqlite_on_conflict="IGNORE"),)


class TextMetadata(TimestampMixin, Base):
    """
    Written Text Metadata
    """

    __tablename__ = "text_metadatas"

    id = Column(
        String,
        ForeignKey("text_contents.id", ondelete="CASCADE"),
        primary_key=True,
    )
    content_type = Column(Enum(WrittenContentCategory))
    author = Column(
        String, ForeignKey("text_authors.id", ondelete="CASCADE"), index=True
    )
    platform = Column(
        String, ForeignKey("platforms.id", ondelete="CASCADE"), index=True
    )
    converation_native_id = Column(String)
    publication_date = Column(DateTime)
    publically_available = Column(Boolean)
    keywords = Column(String)
    miscellanous = Column(String)
    __table_args__ = (UniqueConstraint("id", sqlite_on_conflict="IGNORE"),)


class TextAuthor(TimestampMixin, Base):
    """
    Written Text Author
    """

    __tablename__ = "text_authors"

    id = Column(String, primary_key=True)
    username = Column(String)
