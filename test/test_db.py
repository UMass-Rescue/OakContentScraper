import pytest
import os
from sqlalchemy.orm import close_all_sessions
import content_scraper.db as db
import content_scraper.db.models as models


@pytest.fixture(scope="function", autouse=True)
def dbm(request):
    db.create_db()
    yield
    close_all_sessions()
    db.drop_all()
    db.delete_db()
    assert not os.path.exists(db.sqlite_path)


def test_sqlite_exists():
    assert os.path.exists(db.sqlite_path)


def test_session():
    name = "test_platform"
    session = db.get_session()
    session.add(models.Platform(name=name))
    session.commit()
    result = session.query(models.Platform).all()
    assert len(result) == 1
    assert result[0].name == name
    session.close()
