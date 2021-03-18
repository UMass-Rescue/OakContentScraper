import os
import content_scraper.db as db
import content_scraper.db.models as models


def test_sqlite_exists():
    assert os.path.exists(db.sqlite_path)


def test_session():
    name = "test_platform"
    session = db.get_session()
    session.add(models.SourcePlatform(name=name))
    session.commit()
    result = session.query(models.SourcePlatform).all()
    assert len(result) == 1
    assert result[0].name == name
    session.close()
