from random import randrange
from collections import Counter

class FileService(object):
    def random_line(self, content):
        return content[randrange(0, len(content) -1)]

    def highest_occurrence(self, line):
        wc = Counter(line)
        s = max(wc.values())
        del wc[' ']
        values = [x for x in dict(wc.most_common())]

        return values[0]
