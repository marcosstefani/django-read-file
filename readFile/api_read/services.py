from random import randrange

class FileService(object):
    def random_line(self, content):
        return content[randrange(0, len(content) -1)]
        # line = 0
        # for i in content:
        #     line += 1
        #     print(str(line).strip() + ": " + i)