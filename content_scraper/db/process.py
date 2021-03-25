import content_scraper.db as db
import content_scraper.db.models as models
import json

# from loguru import logger


def persist_app_target(app_metadata, session=db.get_session()):
    target = models.AppTarget(name=app_metadata.name, bundle_id=app_metadata.bundle_id)
    session.add(target)
    session.flush()

    metadata = models.AppMetadata(
        id=target.name,
        publisher=app_metadata.publisher,
        esrb_rating=app_metadata.esrb_rating,
        publication_date=app_metadata.publication_date,
    )

    session.add(metadata)
    session.flush()

    return True


def persist_scrape_result(scrape_result, session=db.get_session()):
    """Short summary.

    :param ScrapeResult scrape_result: pydantic scrape result model
    :param Session session: sqlalchemy session
    :return: True if success
    :rtype: boolean
    """
    source_platform = (
        session.query(models.SourcePlatform)
        .filter(models.SourcePlatform.name == scrape_result.source_platform)
        .first()
    )
    if source_platform is None:
        source_platform = models.SourcePlatform(name=scrape_result.source_platform)
        session.add(source_platform)
        session.flush()

    if scrape_result.app_target:
        app_target = (
            session.query(models.AppTarget)
            .filter(models.AppTarget.name == scrape_result.app_target)
            .first()
        )

    for text_content in scrape_result.contents:
        TextContent = models.TextContent(content=text_content.content)
        session.add(TextContent)
        session.flush()
        if scrape_result.app_target:
            ATA = models.AppTextAssociation(
                text_id=TextContent.id, app_id=app_target.id
            )
            session.add(ATA)

        ta_id = models.generate_uuid()
        TextAuthor = models.TextAuthor(
            id=ta_id,
            username=text_content.author_username,
            source_platform=source_platform.id,
        )
        session.add(TextAuthor)
        session.flush()

        TextMetadata = models.TextMetadata(
            id=TextContent.id,
            content_type=scrape_result.content_type,
            author=ta_id,
            source_platform=source_platform.id,
            conversation_native_id=text_content.conversation_native_id,
            publication_date=text_content.publication_date,
            publically_available=text_content.publically_available,
            native_id=text_content.native_id,
            keywords=json.dumps(text_content.keywords),
            miscellanous=json.dumps(text_content.miscellanous),
        )
        session.add(TextMetadata)

        session.commit()

    return True
