from content_scraper.scrapers import get_scraper
from content_scraper.db.process import persist_scrape_result
from content_scraper.db import get_session
from loguru import logger


def batch_collect_single_platform(platform):

    scraper = get_scraper(platform)
    ScrapeResult = scraper.collect_batch()
    session = get_session()
    try:
        persist_scrape_result(ScrapeResult, session)
    except Exception:
        logger.exception("failed to persist result")
    finally:
        session.commit()
        session.close()

    return True