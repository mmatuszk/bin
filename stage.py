#!/usr/bin/python3.9
from pathlib import Path
from shutil import copytree, ignore_patterns, rmtree
import os, os.path, sys

homedir = str(Path.home())

# configure all the directories
storedir = 'store'
stagedir = 'store801'
htmldir = os.path.join(homedir, 'public_html')
uploadsdir = os.path.join('wp-content', 'uploads')


# copy all the folders except uploads

srcdir = os.path.join(htmldir, storedir)
destdir = os.path.join(htmldir, stagedir)

print(srcdir)
print(destdir)

# remove previously copied store
if (os.path.exists(destdir)):
    rmtree(destdir)

print('copying everything except uploads')
copytree(srcdir, destdir, ignore=ignore_patterns('uploads'))

# copy uploads without photos

srcdir = os.path.join(htmldir, storedir, uploadsdir)
destdir = os.path.join(htmldir, stagedir, uploadsdir)


print('copying uploads except photo library')
copytree(srcdir, destdir, ignore=ignore_patterns('2010', '2013', '2014',
            '2017', '2018', '2019', '2020', '2021', '2022'))
