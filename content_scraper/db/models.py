"""
Content Scraper models
"""
from sqlalchemy import Column, ForeignKey, String, UniqueConstraint, Enum
from sqlalchemy.types import DateTime, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func
from content_scraper.db.strings import WrittenContentCategory
from uuid import uuid4


Base = declarative_base()


class TimestampMixin(object):
    """Provides auto generating created_at field"""

    created_at = Column(DateTime, default=func.now())


class AppMetadata(TimestampMixin, Base):
    __tablename__ = "app_metadatas"

    id = Column(
        String,
        ForeignKey("app_targets.name", ondelete="CASCADE"),
        primary_key=True,
    )
    publisher = Column(String)
    esrb_rating = Column(String)
    publication_date = Column(DateTime)

    __table_args__ = (UniqueConstraint("id", sqlite_on_conflict="IGNORE"),)


class AppTarget(TimestampMixin, Base):
    __tablename__ = "app_targets"

    id = Column(String, primary_key=True, default=str(uuid4()))
    name = Column(String)
    bundle_id = Column(String)
    __table_args__ = (UniqueConstraint("name", sqlite_on_conflict="IGNORE"),)


class AppTextAssociation(TimestampMixin, Base):
    __tablename__ = "app_text_associations"

    id = Column(String, primary_key=True, default=str(uuid4()))
    text_id = Column(
        String, ForeignKey("text_contents.id", ondelete="CASCADE"), index=True
    )
    app_id = Column(String, ForeignKey("app_targets.id", ondelete="CASCADE"))
    __table_args__ = (
        UniqueConstraint("text_id", "app_id", sqlite_on_conflict="IGNORE"),
    )


class SourcePlatform(TimestampMixin, Base):
    """
    Source platforms
    """

    __tablename__ = "source_platforms"

    id = Column(String, primary_key=True, default=str(uuid4()))
    name = Column(String)
    __table_args__ = (UniqueConstraint("name", sqlite_on_conflict="IGNORE"),)


class TextAuthor(TimestampMixin, Base):
    """
    Written Text Author
    """

    __tablename__ = "text_authors"

    id = Column(String, primary_key=True, default=str(uuid4()))
    username = Column(String)
    source_platform = Column(
        String, ForeignKey("source_platforms.id", ondelete="CASCADE")
    )

    __table_args__ = (
        UniqueConstraint("username", "source_platform", sqlite_on_conflict="IGNORE"),
    )


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
    source_platform = Column(
        String, ForeignKey("source_platforms.id", ondelete="CASCADE"), index=True
    )
    converation_native_id = Column(String)
    publication_date = Column(DateTime)
    publically_available = Column(Boolean)
    keywords = Column(String)
    miscellanous = Column(String)
    __table_args__ = (UniqueConstraint("id", sqlite_on_conflict="IGNORE"),)
