from content_scraper import setup_logging
from dotenv import load_dotenv
import content_scraper.pipelines.single as single
import argparse


load_dotenv()
setup_logging()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Perform a text scrape")
    parser.add_argument(
        "platform",
        type=str,
        help="a platform to scrape from various text input sources",
    )
    parser.add_argument(
        "-l",
        "--limit",
        type=int,
        help="number of texts per keyword",
    )
    args = parser.parse_args()

    single.batch_collect_single_platform(args.platform, limit=args.limit)

    print("Single collection complete")
