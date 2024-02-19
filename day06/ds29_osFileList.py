# file: ds29_osFileList.py
# desc: 윈도우 파일 리스트

import os

fnameAry = []
folderName = 'C:\Sources\ds-and-algorithm-2024\day06'

for dirName, subDirList, fnames in os.walk(folderName):
    for fname in fnames:
        fnames.append(fname)


print(fnameAry)
print(len(fnameAry))

fnameAry.sort(reverse=True)
print(fnameAry)