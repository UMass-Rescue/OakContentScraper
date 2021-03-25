from content_scraper.scrapers.utils import Scrape, vdir
from content_scraper.db.standards import ScrapeResult, TextContent
from content_scraper.db.strings import WrittenContentCategory
from datetime import datetime
from loguru import logger
import twint
from tqdm import tqdm


class TwitterScrape(Scrape):
    def __init__(self):
        pass

    def collect_batch(self, keywords, limit, app_target):
        c = twint.Config()

        contents = list()
        tweets = list()
        for keyword in tqdm(keywords):
            logger.debug(f"Searching for... {keyword}")
            c = twint.Config()
            if keyword[0] == "*":
                search = f'"{keyword[1:]}"'
            else:
                search = keyword

            if app_target:
                search += f' "{app_target}"'

            c.Search = search
            c.Limit = limit
            c.Store_object = True
            c.Hide_output = True
            tweets.extend(twint.output.tweets_list)
            twint.run.Search(c)

        for tweet in tweets[: limit * len(keywords)]:
            kws = list()
            for words in keywords:
                if words[0] == "*":
                    kw_list = [words[1:]]
                else:
                    kw_list = words.split(" ")
                for word in kw_list:
                    if word in tweet.tweet:
                        kws.append(word)
            publication_date = datetime.strptime(
                f"{tweet.datestamp} {tweet.timestamp}", "%Y-%m-%d %H:%M:%S"
            )
            misc = dict()
            for attr in vdir(tweet):
                misc[attr] = getattr(tweet, attr)
            contents.append(
                TextContent(
                    native_id=tweet.id,
                    content=tweet.tweet,
                    author_username=tweet.username,
                    conversation_native_id=tweet.conversation_id,
                    publication_date=publication_date,
                    publically_available=True,
                    keywords=kws,
                    miscellanous=str(misc),
                )
            )

        result = ScrapeResult(
            source_platform="twitter",
            contents=contents,
            content_type=WrittenContentCategory.tweet,
            app_target=app_target,
        )
        return result

    def batch_monitor(self, keywords):
        pass

    def continuous_monitor(self, keywords):
        pass
