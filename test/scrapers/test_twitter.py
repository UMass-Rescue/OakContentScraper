import content_scraper.pipelines.single as single
import content_scraper.db as db
import content_scraper.db.models as models


def test_record_exists():
    limit = 5
    single.batch_collect_single_platform("twitter", keywords=["cp"], limit=limit)

    session = db.get_session()
    assert len(session.query(models.SourcePlatform).all()) == 1
    assert len(session.query(models.TextContent).all()) == limit
    assert len(session.query(models.TextAuthor).all()) == limit
    assert len(session.query(models.TextMetadata).all()) == limit


def test_over_limit():
    limit = 110
    single.batch_collect_single_platform("twitter", keywords=["cp"], limit=limit)
    session = db.get_session()
    assert len(session.query(models.SourcePlatform).all()) == 1
    assert len(session.query(models.TextContent).all()) == limit
    assert len(session.query(models.TextAuthor).all()) == limit
    assert len(session.query(models.TextMetadata).all()) == limit
