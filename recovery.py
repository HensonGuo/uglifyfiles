# -*- coding: utf-8 -*-

import os
import time, json

def getAllFiles(dir):
    filesmap = {}
    for root, dirs, files in os.walk(dir):
        filesmap[root.decode('gbk')] = files
    return filesmap

def getOrgnames(recordFile):
    if os.path.exists(recordFile):
        with open(recordFile, 'r') as f:
            orgnames = json.loads(f.read())
            f.close()
            return orgnames

def recoverFile(dir, files, orgnames):
    for file in files:
        if file not in orgnames:
            continue
        orgname = orgnames[file]
        src = os.path.join(dir, file)
        des = os.path.join(dir, orgname)
        os.rename(src, des)
        print u'{}---recovery to---{}'.format(src, des)

def process(handDir, recordFile):
    filesmap = getAllFiles(handDir)
    for dir in filesmap:
        files = filesmap[dir]
        orgnames = getOrgnames(recordFile)
        recoverFile(dir, files, orgnames)
        time.sleep(0.2)

    if os.path.exists(recordFile):
        os.remove(recordFile)

if __name__ == "__main__":
    process('../_test', '../record')
