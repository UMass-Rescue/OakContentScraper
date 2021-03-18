from content_scraper.scrapers.twitter import TwitterScrape
import os
from abc import ABC, abstractmethod


class Scrape(ABC):
    @abstractmethod
    def collect_batch(self):
        pass

    @abstractmethod
    def batch_monitor(self):
        pass

    @abstractmethod
    def continuous_monitor(self):
        pass


def get_scraper(platform_string):
    if platform_string.lower() == "twitter":
        return TwitterScrape()
    else:
        raise LookupError("No scraper for this platform")


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
