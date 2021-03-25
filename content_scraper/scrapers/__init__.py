from content_scraper.scrapers.twitter import TwitterScrape


def get_scraper(platform_string):
    """Delegate Scraper class"""
    if platform_string.lower() == "twitter":
        return TwitterScrape()
    else:
        raise LookupError("No scraper for this platform")
