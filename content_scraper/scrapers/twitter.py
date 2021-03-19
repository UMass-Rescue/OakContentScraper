from content_scraper.scrapers.utils import Scrape, get_all_keywords
from content_scraper.db.standards import ScrapeResult, TextContent
from content_scraper.db.strings import WrittenContentCategory
from datetime import datetime

# import twint
#
# # Configure
# c = twint.Config()
# c.Search = "fruit"
#
# # Run
# twint.run.Search(c)


class TwitterScrape(Scrape):
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
            source_platform="twitter",
            contents=[sample_text],
            content_type=WrittenContentCategory.tweet,
        )
        return result

    def batch_monitor(self, keywords=get_all_keywords()):
        pass

    def continuous_monitor(self, keywords=get_all_keywords()):
        pass
