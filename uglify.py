# -*- coding: utf-8 -*-

import os
import hashlib
import time, json

def getAllFiles(dir, filterFormats):
    filesmap = {}
    for root, dirs, files in os.walk(dir):
        filesmap[root] = []
        for file in files:
            if os.path.splitext(file)[1] in filterFormats:
                filesmap[root].append(file)
    return filesmap

def getMD5Vaule(src):
    md5 = hashlib.md5()
    md5.update(src)
    digest = md5.hexdigest()
    return digest

def changeFileName2MD5(dir, files, recordmap):
    for file in files:
        md5 = getMD5Vaule(file)
        recordmap[md5] = file
        src = os.path.join(dir, file)
        des = os.path.join(dir, md5)
        os.rename(src, des)
        print u'{}---rename to---{}'.format(src, des)

def process(handDir, filterFormats, recordFile):
    filesmap = getAllFiles(handDir, filterFormats)
    md5map = {}
    for dir in filesmap:
        files = filesmap[dir]
        changeFileName2MD5(dir, files, md5map)
        time.sleep(0.2)

    if os.path.exists(recordFile):
        with open(recordFile, 'r') as f:
            orgData = json.loads(f.read())
            f.close()
            md5map = dict(orgData, **md5map)
    with open(recordFile, 'w') as f:
        f.write(json.dumps(md5map))
        f.close()


if __name__ == "__main__":
    process('../_test', ['.txt'], '../record')