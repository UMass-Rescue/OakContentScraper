import pytest
import os
from sqlalchemy.orm import close_all_sessions
from content_scraper.db import DBManager


@pytest.fixture(scope="function", autouse=True)
def dbm(request):
    dbm = DBManager()
    yield dbm
    close_all_sessions()
    dbm.drop_all()
    dbm.delete_db()
    assert not os.path.exists(dbm.sqlite_path)


def test_sqlite_exists(dbm):
    assert os.path.exists(dbm.sqlite_path)
