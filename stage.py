#!/usr/bin/python
from pathlib import Path
from shutil import copytree, ignore_patterns, rmtree
import os, os.path

homedir = str(Path.home())
print(homedir)
print(os.getcwd())

# configure all the directories
storedir = 'store'
stagedir = 'store801'
htmldir = os.path.join(homedir, 'Documents', 'test',)
uploadsdir = os.path.join('wp-content', 'uploads')


# copy all the folders except uploads

srcdir = os.path.join(htmldir, storedir)
destdir = os.path.join(htmldir, stagedir)

# remove previously copied store
rmtree(destdir)

copytree(srcdir, destdir, ignore=ignore_patterns('uploads'))
print(srcdir, destdir)

# copy uploads without photos

srcdir = os.path.join(htmldir, storedir, uploadsdir)
destdir = os.path.join(htmldir, stagedir, uploadsdir)
copytree(srcdir, destdir, ignore=ignore_patterns('2010', '2013', '2014',
            '2017', '2018', '2019', '2020', '2021', '2022'))
