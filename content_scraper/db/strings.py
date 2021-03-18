from enum import Enum


class WrittenContentCategory(Enum):
    """Possible sources for written content"""

    direct_message = "direct_message"
    tweet = "tweet"
    review = "review"
    wall_post = "wall_post"
