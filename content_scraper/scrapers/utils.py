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


def vdir(obj):
    return [x for x in dir(obj) if not x.startswith("__")]
