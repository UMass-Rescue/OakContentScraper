import content_scraper.db as db
import content_scraper.db.models as models
from loguru import logger


def persist_scrape_result(scrape_result, session=db.get_session()):
    """Short summary.

    :param ScrapeResult scrape_result: pydantic scrape result model
    :param Session session: sqlalchemy session
    :return: True if success
    :rtype: boolean
    """
    platform = models.Platform(name=scrape_result.platform)
    session.add(platform)
    session.flush()
    logger.info(platform.id)

    return True
