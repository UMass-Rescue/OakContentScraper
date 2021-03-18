# from content_scraper.scrapers import get_all_keywords
from content_scraper.db.standards import ScrapeResult, TextContent
from content_scraper.db.strings import WrittenContentCategory
from datetime import datetime
import os

# import twint
#
# # Configure
# c = twint.Config()
# c.Search = "fruit"
#
# # Run
# twint.run.Search(c)


def get_all_keywords():
    keyword_dir = os.path.join(
        os.path.dirname(__file__), "..", "..", "resources", "keywords"
    )
    keywords = list()
    for file in os.listdir(keyword_dir):
        if file.split(".")[-1] == "txt":
            keywords.extend(get_keywords_from_file(keyword_dir, file))
    return keywords


def get_keywords_from_file(directory, filename):
    keywords = list()
    with open(os.path.join(directory, filename), "r") as datafile:
        for line in datafile:
            keywords.extend(line)
    return keywords


class TwitterScrape:
    def __init__(self):
        pass

    def collect_batch(self, keywords=get_all_keywords()):
        sample_text = TextContent(
            content="hi",
            author_username="hi",
            conversation_native_id="test",
            publication_date=datetime.now(),
            publically_available=True,
            keywords=["Hi"],
            miscellanous="hi",
        )

        result = ScrapeResult(
            platform="twitter",
            contents=[sample_text],
            content_type=WrittenContentCategory.tweet,
        )
        return result

    def batch_monitor(self, keywords=get_all_keywords()):
        pass

    def continuous_monitor(self, keywords=get_all_keywords()):
        pass
