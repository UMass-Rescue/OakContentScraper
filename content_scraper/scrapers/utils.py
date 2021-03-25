from abc import ABC, abstractmethod


class Scrape(ABC):
    @abstractmethod
    def collect_batch(self):
        """Collect batch of text contents"""
        pass

    @abstractmethod
    def batch_monitor(self):
        pass

    @abstractmethod
    def continuous_monitor(self):
        pass


def vdir(obj):
    """Short summary.

    :param any obj: Any object
    :return: List of object attributes
    :rtype: list

    """
    return [x for x in dir(obj) if not x.startswith("__")]
