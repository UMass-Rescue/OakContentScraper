"""
Content Scraper models
"""
from sqlalchemy import Column, ForeignKey, String, UniqueConstraint, Enum
from sqlalchemy.types import DateTime, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func
from content_scraper.db.util import WrittenContentCategory
from uuid import uuid4


Base = declarative_base()


class TimestampMixin(object):
    """Provides auto generating created_at field"""

    created_at = Column(DateTime, default=func.now())


class Platform(TimestampMixin, Base):
    """
    Source platforms
    """

    __tablename__ = "platforms"

    id = Column(String, primary_key=True, default=str(uuid4()))
    name = Column(String)
    __table_args__ = (UniqueConstraint("name", sqlite_on_conflict="IGNORE"),)


class TextContent(TimestampMixin, Base):
    """
    Written Text Content
    """

    __tablename__ = "text_contents"

    id = Column(String, primary_key=True, default=str(uuid4()))
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
        default=str(uuid4()),
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

    id = Column(String, primary_key=True, default=str(uuid4()))
    username = Column(String)
    platform = Column(String, ForeignKey("platforms.id", ondelete="CASCADE"))

    __table_args__ = (
        UniqueConstraint("username", "platform", sqlite_on_conflict="IGNORE"),
    )
