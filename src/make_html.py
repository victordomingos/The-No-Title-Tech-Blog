#!/usr/bin/env python
import os

from pelican import Pelican
from pelican.settings import read_settings

print '\nReading the publish settings file.\n'
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

settings_filepath = os.path.expanduser(dname+"/publishconf.py")
settings = read_settings(settings_filepath)

print 'Building the website with Pelican...\n'
pelican = Pelican(settings)
pelican.run()
