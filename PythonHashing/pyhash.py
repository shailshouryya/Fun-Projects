import os
import hashlib
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("file")
args = parser.parse_args()

md5 = hashlib.md5()
sha1 = hashlib.sha1()

try:
    with open(args.file, 'rb') as f:
        buf = f.read()
        md5.update(buf)
        sha1.update(buf)
    print("{} {} {}".format(os.path.basename(args.file), md5.hexdigest(), sha1.hexdigest()))
except FileNotFoundError as e:
    print(e)