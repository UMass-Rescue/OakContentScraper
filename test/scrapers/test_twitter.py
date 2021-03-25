import content_scraper.pipelines.single as single
import content_scraper.db as db
import content_scraper.db.models as models


def test_record_exists():

    single.batch_collect_single_platform("twitter", keywords=["cp"], limit=5)
    session = db.get_session()
    assert len(session.query(models.SourcePlatform).all()) == 1
    assert len(session.query(models.TextContent).all()) == 5
    assert len(session.query(models.TextAuthor).all()) == 5
    assert len(session.query(models.TextMetadata).all()) == 5
