import os

def makefiledir(out):
    dirname = os.path.dirname(out)
    if dirname != "": os.makedirs(dirname, exist_ok=True)

