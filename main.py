import glob

from search import search
from tags import tags

fpath = u"mp3/*.m4a"
print(fpath)

files = glob.glob(fpath)

for fname in files:
    if fname.endswith('.m4a'):
        print(fname)
        search(fname)
