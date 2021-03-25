import os


def get_all_keywords():
    keyword_dir = os.path.join(
        os.path.dirname(__file__), "..", "..", "resources", "keywords"
    )
    keywords = list()
    for file in os.listdir(keyword_dir):
        if file.split(".")[-1] == "txt":
            kws = get_keywords_from_file(keyword_dir, file)
            keywords.extend(kws)
    return keywords


def get_keywords_from_file(directory, filename):
    keywords = list()
    with open(os.path.join(directory, filename), "r") as datafile:
        for line in datafile:
            keywords.append(line.rstrip("\r\n"))
    return keywords
