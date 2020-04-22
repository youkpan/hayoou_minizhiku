# encoding=utf-8
import sys
sys.path.append('../')

import jieba
import jieba.analyse
from optparse import OptionParser

ignorlist = ["朋友圈","天前"]
ignordict = {}
for w in ignorlist:
    ignordict[w] = 1

def is_all_chinese(strs):
    for _char in strs:
        if not '\u4e00' <= _char <= '\u9fa5':
            return False
    return True

USAGE = "usage:    python extract_tags_with_weight.py [file name] -k [top k] -w [with weight=1 or 0]"

parser = OptionParser(USAGE)
parser.add_option("-k", dest="topK")
parser.add_option("-w", dest="withWeight")
opt, args = parser.parse_args()


if len(args) <1:
    print(USAGE)
    sys.exit(1)

file_name = args[0]

if opt.topK is None:
    topK = 10
else:
    topK = int(opt.topK)

if opt.withWeight is None:
    withWeight = False
else:
    if int(opt.withWeight) is 1:
        withWeight = True
    else:
        withWeight = False

content = open(file_name, 'rb').read()

 

tags = jieba.analyse.extract_tags(content, topK=topK, withWeight=withWeight)

if withWeight is True:
    for tag in tags:
        word = tag[0]
        weight = tag[1]
        if is_all_chinese(tag[0]):
            try:
                t = ignordict[word]
            except Exception as e:
                print("tag: %s\t\t weight: %f" % (word,weight))

else:
    print(",".join(tags))


'''
with  open(fname, "r+") as f:
    for line in f:
'''
        