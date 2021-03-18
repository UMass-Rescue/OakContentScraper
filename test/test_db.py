import pytest
import os
from sqlalchemy.orm import close_all_sessions
import content_scraper.db as db


@pytest.fixture(scope="function", autouse=True)
def dbm(request):
    yield
    close_all_sessions()
    db.drop_all()
    db.delete_db()
    assert not os.path.exists(db.sqlite_path)


def test_sqlite_exists():
    assert os.path.exists(db.sqlite_path)
