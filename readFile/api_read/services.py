from random import randrange

class FileService(object):
    def random_line(self, content):
        return content[randrange(0, len(content) -1)]